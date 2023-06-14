import asyncio
import matplotlib.pyplot as plt
from ib_insync import IB, Contract, TickByTickAllLast

async def market_data():
    ib = IB()
    await ib.connectAsync('localhost', 4002, clientId=1)

    contract = Contract(conId=604258925, symbol='FDAX', secType='FUT', exchange='EUREX', currency='EUR')
    await ib.qualifyContractsAsync(contract)

    ticker = ib.reqTickByTickData(contract, 'AllLast')

    # Store the timestamp and price in separate lists
    timestamps = []
    prices = []

    # Print the latest tick data immediately and plot the prices
    while True:
        await asyncio.sleep(2)
        timestamp = ticker.time
        price = ticker.last
        print(timestamp, price)

        timestamps.append(timestamp)
        prices.append(price)

        # Plot the prices as a line plot
        plt.plot(timestamps, prices)
        plt.xlabel('Timestamp')
        plt.ylabel('Price')
        plt.title('Price Plot')
        plt.grid(True)
        plt.pause(0.01)
        plt.clf()

def main():
    asyncio.run(market_data())

if __name__ == '__main__':
    main()
