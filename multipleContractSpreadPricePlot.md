# Real-Time Price and Spread Plotting with IB-InSync

This script provides an example of how to use the `ib_insync` library to request real-time tick-by-tick data from Interactive Brokers (IB) and plot the prices of two contracts as well as the spread between them. The script connects to the TWS (Trader Workstation) or Gateway application via the IB API and continuously updates the price plots based on the received tick data.
![image](https://github.com/jamiePDunne/ibTrading/assets/83908748/bb4c34f3-2e30-4301-95d3-b6b668f37afd)

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- `ib_insync` library installed (`pip install ib_insync`)
- Access to the TWS or Gateway application provided by Interactive Brokers

## Getting Started

1. Import the necessary modules:

```python
import asyncio
import matplotlib.pyplot as plt
from ib_insync import IB, Contract, TickByTickAllLast
```

2. Define an `async` function, `market_data()`, to handle the real-time data retrieval and plotting:

```python
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
    spreads = []

    # Create subplots for each contract's price plot and the spread plot
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

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

    # Set labels and titles for the third subplot (spread plot)
    ax3.set_xlabel('Timestamp')
    ax3.set_ylabel('Spread')
    ax3.set_title('Spread Plot')
    ax3.grid(True)

    while True:
        # Pause execution for 2 seconds
        await asyncio.sleep(2)

        # Get the latest timestamp and price for contract 1
        timestamp1 = ticker1.time
        price1 = ticker1.last
        print('Contract 1:', timestamp1, price1)

        # Get the latest timestamp and price for contract 2
        timestamp2 = ticker2.time
        price2 = ticker2.last
        print('Contract 2:', timestamp2, price2)

        # Skip calculation if any price is NaN
        if price1 is None or price2 is None:
            continue

        # Add the timestamp and price to the respective lists for contract 1
        timestamps1.append(timestamp1)


        prices1.append(price1)

        # Add the timestamp and price to the respective lists for contract 2
        timestamps2.append(timestamp2)
        prices2.append(price2)

        # Calculate the spread between the two contracts
        spread = price1 - price2
        spreads.append(spread)

        # Plot the prices for contract 1
        ax1.plot(timestamps1, prices1, color='blue')
        ax1.figure.canvas.draw()

        # Plot the prices for contract 2
        ax2.plot(timestamps2, prices2, color='red')
        ax2.figure.canvas.draw()

        # Plot the spread
        ax3.plot(timestamps2, spreads, color='green')
        ax3.figure.canvas.draw()

        # Pause briefly to update the plots
        plt.pause(0.01)
```

3. Create an `async` function, `main()`, to run the `market_data()` function within the default event loop:

```python
async def main():
    # Run the market_data function within the default event loop
    await market_data()
```

4. Run the `main()` function within the `__main__` block to start the script:

```python
if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
```

## Customization

- Modify the connection settings (`localhost`, `4002`, `clientId`) in the `ib.connectAsync()` line to match your TWS or Gateway configuration.
- Adjust the contract details (`conId`, `symbol`, `secType`, `exchange`, `currency`) for `contract1` and `contract2` to match your desired contracts.
- Customize the plot labels, titles, colors, and other styling options to suit your preferences.

## Notes

- The script uses the `ib_insync` library to connect to the TWS or Gateway application and retrieve real-time tick-by-tick data. Make sure you have a valid connection to the IB API before running the script.
- The script assumes you have the necessary permissions and access to trade the specified contracts. Ensure that you have the proper permissions and account configuration to access the contract data.
- The script plots the prices and spread in real-time using the `matplotlib` library. The plots are updated every 2 seconds, but you can adjust the update frequency by modifying the sleep duration in the `await asyncio.sleep(2)` line.
- The spread is calculated as the difference between `contract1` last price and `contract2` last price. If either price is `None`, indicating a missing price, the calculation of the spread is skipped for that iteration to avoid incorrect spread values.
- The script can be customized further to include additional plots, indicators, or features based on your requirements.

