import os
import glob
import pandas as pd
import time

DIRECTORY = "ADD PATH"  # Directory for CSV files


def get_most_recent_csv():
    files = glob.glob(os.path.join(DIRECTORY, "FDAX*.csv"))
    if files:
        return max(files, key=os.path.getctime)
    else:
        return None


def compute_table(wait_time):
    while True:
        file_name = get_most_recent_csv()
        if file_name:
            df = pd.read_csv(file_name)

            # Compute the simple moving average (SMA) of the last 200 Last values
            df['SMA'] = df['Last'].rolling(window=200).mean()
            df['SD'] = df['Last'].rolling(window=200).std()
            df['Z'] = (df['Last']- df['SMA'])/df['SD']

            # Save the computed values to a new CSV file
            file_base = os.path.basename(file_name)
            new_file_name = os.path.join(DIRECTORY, f"computed_{file_base}")
            df.to_csv(new_file_name, index=False)

            print(f"Computed values saved to: {new_file_name}")

            last_update_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Last update time: {last_update_time}")

        time.sleep(wait_time)


if __name__ == '__main__':
    wait_time_seconds = 10  # Set the wait time in seconds
    compute_table(wait_time_seconds)
