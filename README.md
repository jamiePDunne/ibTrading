# ibTrading

# Interactive Data Subscriptions

This GitHub repository contains various scripts for working with Interactive Data Subscriptions from Interactive Brokers (IB) TWS or Gateway. These scripts provide functionality to subscribe to real-time market data, receive updates, and perform analysis on the streaming data.

## Prerequisites

- Python 3.7 or higher
- `ib_insync` library
- Interactive Brokers account with TWS or Gateway configured

## Installation

1. Clone this repository or download the script files.
2. Install the required dependencies by running the following command:

   ```
   pip install ib_insync
   ```

## Usage

To use these scripts, follow the steps below:

1. Make sure your Interactive Brokers TWS or Gateway is running and connected.
2. Navigate to the desired script file.
3. Modify the script variables, such as contract details and subscription parameters, as per your requirements.
4. Run the script using the following command:

   ```
   python <script_name>.py
   ```

   Note: Replace `<script_name>.py` with the actual script filename you want to execute.

5. The script will connect to Interactive Brokers, subscribe to the specified market data, and start receiving updates.
6. Depending on the script, you can analyze the data, log it to a file, or visualize it for further analysis.

## Troubleshooting

If you encounter any issues while running the scripts, make sure to check the following:

- Ensure that your Interactive Brokers TWS or Gateway is running and properly connected.
- Verify that you have the necessary permissions and subscription rights for the requested market data.
- Double-check the contract details, such as conId, exchange, secType, and currency, to ensure they match the desired contract.
- Review the Interactive Brokers API documentation and error messages for troubleshooting specific issues.

## Disclaimer

Please note that the use of these scripts and the Interactive Data Subscriptions is subject to the terms and conditions of Interactive Brokers. Ensure that you comply with their data usage policies and any applicable regulations.

## License

The scripts in this repository are licensed under the [MIT License](LICENSE). Feel free to modify and use them according to your needs.
