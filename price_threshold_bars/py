import os
import pandas as pd
import logging


def downsample_file(source_file, dest_file, threshold):
    """
    Downsample a file containing price data based on a given threshold.

    Args:
        source_file (str): Path to the source file.
        dest_file (str): Path to save the downsampled file.
        threshold (float): Price threshold for downsampling.

    Returns:
        None
    """
    try:
        # Read the source file
        df = pd.read_csv(source_file)

        # Convert TIMESTAMP column to datetime type
        df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

        # Sort the DataFrame by TIMESTAMP column
        df.sort_values('TIMESTAMP', inplace=True)

        # Compute the downsampled data
        downsampled = []
        prev_close = None
        price_points = []

        for _, row in df.iterrows():
            timestamp = row['TIMESTAMP']
            price = row['PRICE']

            if prev_close is None:
                # First row
                prev_close = price
                price_points.append(price)
                continue

            if price >= prev_close + threshold or price <= prev_close - threshold:
                # Compute OHLCV and IS_GAUSSIAN values for the previous bar
                if len(price_points) >= 4:
                    open_price = price_points[0]
                    high_price = max(price_points)
                    low_price = min(price_points)
                    close_price = price_points[-1]
                    volume = len(price_points)
                    bar_ticks_count = len(price_points)  # New column

                else:
                    # Not enough price points, assign default values
                    open_price = high_price = low_price = close_price = volume = 0

                # Append the downsampled data to the list
                downsampled.append(
                    [timestamp, close_price, open_price, high_price, low_price, volume])

                # Reset for the next bar
                prev_close = price
                price_points = [price]
            else:
                # Add the price to the current bar
                price_points.append(price)

        # Create a DataFrame from the downsampled data
        downsampled_df = pd.DataFrame(downsampled,
                                      columns=['TIMESTAMP', 'CLOSE', 'OPEN', 'HIGH', 'LOW', 'VOLUME'])

        # Save the downsampled file
        downsampled_df.to_csv(dest_file, index=False)

    except Exception as e:
        logging.error(f"Error processing file: {source_file}. Error: {str(e)}")


def downsample_files(source_folder, destination_folder, threshold):
    """
    Downsample all files in a source folder and save them in a destination folder.

    Args:
        source_folder (str): Path to the source folder.
        destination_folder (str): Path to the destination folder.
        threshold (float): Price threshold for downsampling.

    Returns:
        None
    """
    try:
        # Validate source_folder and destination_folder
        if not os.path.isdir(source_folder):
            raise ValueError("Invalid source folder path.")
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Configure logging
        log_file = os.path.join(destination_folder, 'log.txt')
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

        # Iterate over the files in the source folder
        num_files = 0
        for file in os.listdir(source_folder):
            if file.endswith('.csv'):
                source_file = os.path.join(source_folder, file)
                dest_file = os.path.join(destination_folder, file)

                # Perform down sampling on the file
                downsample_file(source_file, dest_file, threshold)
                num_files += 1

                # Log progress
                logging.info(f"Processed file: {file}")
                print(f"Processed file: {file}")

        # Print total number of files created and saved
        total_files_message = f"Total files created and saved: {num_files}"
        logging.info(total_files_message)
        print(total_files_message)

    except Exception as e:
        logging.error(f"Error downsampling files. Error: {str(e)}")


# Example usage
source_folder_path = '/add folder path here/'
destination_folder_path = '/add folder path here/'
threshold_value = 10

downsample_files(source_folder_path, destination_folder_path, threshold_value)
