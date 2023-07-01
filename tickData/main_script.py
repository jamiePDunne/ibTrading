import csv
from datetime import datetime
from ib_insync import IB, Contract, util
from collections import deque
import os


async def receive_ticks(ib, contract, ring_buffer, interval):
    while True:
        ticker = ib.reqMktData(contract, '', False, False)
        await util.asyncio.sleep(interval)  # Adjust the interval as needed
        if ticker.time and (not ring_buffer or ticker.time != ring_buffer[-1].time):
            ring_buffer.append(ticker)
            print(ticker)  # Print tick update to the console


async def save_tick_data(ring_buffer):
    directory = '/home/jamie/ib_market_data'  # Specify the desired directory path
    file_name = os.path.join(directory, f"FDAX_{datetime.now().strftime('%Y%m%d')}.csv")
    fieldnames = ['Timestamp', 'Last', 'Last Size', 'Bid', 'Ask']

    while True:
        await util.asyncio.sleep(0.1)  # Adjust the sleep duration as needed
        if ring_buffer:
            tick_data = []
            while ring_buffer:
                ticker = ring_buffer.popleft()
                tick_data_row = {
                    'Timestamp': ticker.time,
                    'Last': ticker.last,
                    'Last Size': ticker.lastSize,
                    'Bid': ticker.bid,
                    'Ask': ticker.ask
                }
                tick_data.append(tick_data_row)

            with open(file_name, 'a', newline='') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                if csv_file.tell() == 0:
                    csv_writer.writeheader()  # Write header only if file is empty
                csv_writer.writerows(tick_data)


async def market_data():
    ib = IB()
    await ib.connectAsync('localhost', 4002, clientId=1)

    fdax = 540729664 # sep 2023
    contract = Contract(conId=fdax, symbol='FDAX', secType='FUT', exchange='EUREX', currency='EUR')
    await ib.qualifyContractsAsync(contract)

    ring_buffer = deque(maxlen=1000)
    interval = 5  # Set the desired interval in seconds

    receive_task = util.asyncio.create_task(receive_ticks(ib, contract, ring_buffer, interval))
    save_task = util.asyncio.create_task(save_tick_data(ring_buffer))

    await util.asyncio.gather(receive_task, save_task)


def main():
    util.asyncio.run(market_data())


if __name__ == '__main__':
    main()
