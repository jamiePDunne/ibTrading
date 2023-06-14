import asyncio
import matplotlib.pyplot as plt
from ib_insync import IB, Contract, TickByTickAllLast

async def market_data():
    # Create an IB object and connect to the TWS or Gateway
    ib = IB()
    await ib.connectAsync('localhost', 4002, clientId=1)

    # Define the first contract
    contract1 = Contract(conId=604258925, symbol='FDAX', secType='FUT', exchange='EUREX', currency='EUR')
    await ib.qualifyContractsAsync(contract1)

    # Define the second contract
    contract2 = Contract(conId=540729504, symbol='FDAX', secType='FUT', exchange='EUREX', currency='EUR')
    await ib.qualifyContractsAsync(contract2)

    # Request tick-by-tick data for both contracts
    ticker1 = ib.reqTickByTickData(contract1, 'AllLast')
    ticker2 = ib.reqTickByTickData(contract2, 'AllLast')

    # Create lists to store timestamps and prices for each contract
    timestamps1 = []
    prices1 = []
    timestamps2 = []
    prices2 = []

    # Create subplots for each contract's price plot
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    # Set labels and titles for the first subplot
    ax1.set_xlabel('Timestamp')
    ax1.set_ylabel('Price')
    ax1.set_title('Price Plot - Contract 1')
    ax1.grid(True)

    # Set labels and titles for the second subplot
    ax2.set_xlabel('Timestamp')
    ax2.set_ylabel('Price')
    ax2.set_title('Price Plot - Contract 2')
    ax2.grid(True)

    while True:
        # Pause execution for 2 seconds
        await asyncio.sleep(2)

        # Get the latest timestamp and price for contract 1
        timestamp1 = ticker1.time
        price1 = ticker1.last
        print('Contract 1:', timestamp1, price1)

        # Add the timestamp and price to the respective lists for contract 1
        timestamps1.append(timestamp1)
        prices1.append(price1)

        # Plot the prices for contract 1
        ax1.plot(timestamps1, prices1, color='blue')
        ax1.figure.canvas.draw()

        # Get the latest timestamp and price for contract 2
        timestamp2 = ticker2.time
        price2 = ticker2.last
        print('Contract 2:', timestamp2, price2)

        # Add the timestamp and price to the respective lists for contract 2
        timestamps2.append(timestamp2)
        prices2.append(price2)

        # Plot the prices for contract 2
        ax2.plot(timestamps2, prices2, color='red')
        ax2.figure.canvas.draw()

        # Pause briefly to update the plots
        plt.pause(0.01)

async def main():
    # Run the market_data function within the default event loop
    await market_data()

if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
