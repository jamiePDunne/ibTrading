# Interactive Brokers Historical Data Downloader

This script allows you to download 1-minute bar historical data for a specific contract from Interactive Brokers (IB) TWS or Gateway. The downloaded data is saved to a CSV file for further analysis and processing.

## Prerequisites

- Python 3.7 or higher
- `ib_insync` library
- Interactive Brokers account with TWS or Gateway configured

## Installation

1. Clone this repository or download the script file.
2. Install the required dependencies by running the following command:

   ```
   pip install ib_insync
   ```

## Configuration

Before running the script, you need to configure the following parameters:

- `start_date`: The start date for the historical data in `datetime` format (yyyy/mm/dd).
- `end_date`: The end date for the historical data in `datetime` format (yyyy/mm/dd).
- `maxIterations`: The maximum number of iterations to retrieve historical data. Default value is 25.
- `fdax_conId`: The contract ID (conId) for the specific contract you want to retrieve data for. You can uncomment the appropriate conId based on the contract month you're interested in.

## Usage

1. Make sure your Interactive Brokers TWS or Gateway is running and connected.
2. Run the script using the following command:

   ```
   python historical_data_downloader.py
   ```

   Note: Replace `historical_data_downloader.py` with the actual script filename if you renamed it.

3. The script will connect to Interactive Brokers and start downloading the 1-minute bar historical data for the specified contract and date range.
4. The downloaded data will be saved to individual CSV files named `TAS_FDAX_1M_YYYYMMDD.csv`, where `YYYYMMDD` represents the date of the data.
5. The CSV files will be saved in the directory specified by the `file_path` variable in the script. You can modify the file path as per your preference.

## Troubleshooting

If you encounter any issues while running the script, here are a few possible reasons and solutions:

- **Insufficient historical data**: It's possible that the specified contract or date range does not have enough historical data available at the 1-minute bar level. In such cases, you may need to adjust the contract or choose a different date range.

- **Incompatible contract details**: Ensure that the contract details, such as conId, exchange, secType, and currency, are correct for the specific contract you are interested in. Verify that the contract details match the available historical data.

- **Non-trading days or holidays**: Certain days might not have any trading activity, resulting in no available historical data. Make sure to exclude non-trading days or holidays from the date range or consider a different contract or date range.

## Disclaimer

Please note that the use of this script and the downloaded historical data is subject to the terms and conditions of Interactive Brokers. Ensure that you comply with their data usage policies and any applicable regulations.

## License

This script is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.
