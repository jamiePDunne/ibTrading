# Market Data Analysis

This Python script connects to the Interactive Brokers (IB) trading platform and retrieves tick-by-tick market data for a specific futures contract. The script then plots the received data in real-time using Matplotlib.

![image](https://github.com/jamiePDunne/ibTrading/assets/83908748/0beb358c-eee8-4c44-af2a-18668a357e44)


## Prerequisites

To run this script, you need to have the following:

- Python installed on your machine
- `ib_insync` library installed. You can install it using `pip install ib_insync`.
- An Interactive Brokers account with API access. Ensure you have the necessary credentials.

## Usage

1. Ensure you have met the prerequisites mentioned above.
2. Replace the placeholder values in the `Contract` object with the appropriate values for your desired futures contract. For example, you can change the `symbol` to 'ES' for E-mini S&P 500 futures or 'NQ' for E-mini Nasdaq 100 futures.
3. Run the script.

The script will connect to the IB trading platform, qualify the contract, and start receiving tick-by-tick data. It will print the timestamp and price of each received tick and plot the prices in real-time on a line graph. The graph will update every two seconds with the latest data.

You can interrupt the script by pressing Ctrl+C in the terminal.

## Notes

- Make sure to have the Interactive Brokers TWS (Trader Workstation) or IB Gateway application running on your machine before executing this script.
- Ensure that the TWS or IB Gateway API settings are configured correctly to allow API connections on the specified port (default: 4002).

## Disclaimer

This script is for educational purposes only and does not constitute financial or investment advice. Use it at your own risk.

## License

This script is released under the MIT License.
