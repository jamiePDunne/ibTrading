
# IB Contract Price Plotter

This script connects to the Interactive Brokers (IB) TWS or Gateway API and retrieves tick-by-tick price data for two contracts. It plots the price data for each contract in separate subplots using Matplotlib.

![image](https://github.com/jamiePDunne/ibTrading/assets/83908748/5e1af9f8-04c2-4474-b390-4f1f29fbcfca)

## Prerequisites

- Python 3.7 or above
- `ib_insync` library (install using `pip install ib_insync`)
- `matplotlib` library (install using `pip install matplotlib`)

## Usage

1. Make sure you have the prerequisites installed.
2. Update the contract details in the script to specify the contracts you want to track. Modify the `contract1` and `contract2` objects with the desired contract details (conId, symbol, secType, exchange, currency).
3. Run the script using the command: `python contract_price_plotter.py`

The script will connect to the IB TWS or Gateway API, retrieve tick-by-tick price data for the specified contracts, and plot the prices in real-time using Matplotlib. The price plots for each contract will be displayed in separate subplots.

## Important Notes

- Ensure that you have the IB TWS or Gateway software running and configured properly.
- Adjust the sleep duration in the script if you want to change the interval between data updates.
- The script assumes that you have an active IB account and the necessary permissions to access the specified contracts.
- The script may display warnings related to the Matplotlib GUI event loop. These warnings can be ignored as they do not affect the functionality of the script.

Feel free to customize the script according to your specific needs.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT).
