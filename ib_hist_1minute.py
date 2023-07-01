import logging
from ib_insync import *
import csv
from datetime import datetime, timedelta, timezone

maxIterations = 25
start_date = datetime(2023, 6, 16)  # yyyy/mm/dd
end_date = datetime(2023, 6, 20)  # yyyy/mm/dd

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to the Interactive Brokers TWS or Gateway
util.startLoop()
ib = IB()
ib.connect('localhost', 4002, clientId=1)  # Replace with your connection details

# Define the unique contract identifier (conId) for FDAX
#fdax_conId = 540729504  # Ju 2023
fdax_conId = 540729664 # sep 2023
# fdax_conId = 540729669 # dec 2023

# Create a contract object for FDAX
contract = Contract(conId=fdax_conId, exchange='EUREX', secType='FUT', currency='EUR')

# Initialize variables
seq_no = 1

# Iterate over each date
current_date = start_date
while current_date <= end_date:
    # Define the start and end date-time for the current date in UTC
    start_date_time = datetime.combine(current_date, datetime.min.time(), tzinfo=timezone.utc)
    end_date_time = datetime.combine(current_date, datetime.max.time(), tzinfo=timezone.utc)

    # Request 1-minute bar historical data for the current date
    bars = ib.reqHistoricalData(
        contract, endDateTime='', durationStr='1 D',
        barSizeSetting='1 min', whatToShow='TRADES',
        useRTH=True, formatDate=1
    )

    # Check if bars list is empty
    if not bars:
        print("Here are a few possible reasons for the error:\n")
        print("Insufficient historical data: It's possible that the specified contract or date range does not have enough historical data available at the 1-minute bar level. In such cases, you may need to adjust the contract or choose a different date range.\n")
        print("Incompatible contract details: Ensure that the contract details, such as conId, exchange, secType, and currency, are correct for the specific contract you are interested in. Verify that the contract details match the available historical data.\n")
        print("Non-trading days or holidays: Certain days might not have any trading activity, resulting in no available historical data. Make sure to exclude non-trading days or holidays from the date range or consider a different contract or date range.\n")
    else:
        # Process and save the retrieved bar data to a CSV file
        file_date = current_date.strftime('%Y%m%d')
        file_path = f'/<add your pth here>/1M_{file_date}.csv'  # Add '1M' before the file date
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['TIMESTAMP', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME'])
            for bar in bars:
                time_str = bar.date.strftime('%Y-%m-%d %H:%M:%S')
                csv_writer.writerow([time_str, bar.open, bar.high, bar.low, bar.close, bar.volume])

        logging.info(f"Saved 1-minute bar data for date: {current_date.date()}")

    current_date += timedelta(days=1)

# Disconnect from Interactive Brokers
ib.disconnect()
