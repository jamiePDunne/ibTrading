**Readme File:**

# Trading Data Analysis Scripts

This repository contains three Python scripts for analyzing and visualizing trading data. These scripts are designed for users with minimal coding experience and are meant to be run in a specific order.

## Summary

The provided scripts utilize a ring buffer approach to efficiently handle and process real-time tick data from the Interactive Brokers API. This approach offers several benefits:

- **Memory efficiency**: The ring buffer implementation allows for efficient memory utilization by limiting the number of tick data records stored at any given time. This is particularly useful when dealing with a continuous stream of real-time data, as it prevents excessive memory consumption.

- **Real-time data handling**: The ring buffer acts as a temporary storage for tick data updates. It enables the scripts to process and analyze the most recent ticks efficiently without the need to store the entire dataset. This approach allows for real-time data analysis while minimizing latency.

- **Seamless data flow**: The scripts, when executed in sequence, create a smooth data flow. The first script retrieves tick data and appends it to the ring buffer, while the subsequent scripts consume the data from the buffer for computation and visualization. This streamlined approach ensures a continuous and synchronized data pipeline.

- **Modular and scalable**: The use of a ring buffer decouples the data retrieval, computation, and visualization processes. Each script focuses on a specific task and can be modified or extended independently. This modularity allows for easy customization and scalability as per the user's requirements.

## Prerequisites

Before running the scripts, please ensure that you have the following dependencies installed:

- Python 3.x
- ib_insync library
- pandas library
- matplotlib library

You can install the necessary dependencies using pip:

```shell
pip install ib_insync pandas matplotlib
```

...

[Continue with the rest of the readme file as previously provided.]

## Script 1: buffer_main_script.py

This script retrieves tick data from a specified financial instrument using the Interactive Brokers API (ib_insync library). It saves the tick data to a CSV file for further analysis.

To run this script, follow these steps:

1. Open `buffer_main_script.py` in a text editor.
2. Locate the line `directory = 'ADD PATH'` and replace `'ADD PATH'` with the desired directory path where you want to save the tick data CSV files.
3. Adjust the `interval` variable if needed. It represents the time interval (in seconds) between each data retrieval.
4. Save the modifications and run the script.

## Script 2: buffer_compute_values.py

This script reads the most recent tick data CSV file generated by `buffer_main_script.py` and computes additional values based on the data. It saves the computed values to a new CSV file.

To run this script, follow these steps:

1. Open `buffer_compute_values.py` in a text editor.
2. Locate the line `DIRECTORY = "ADD PATH"` and replace `'ADD PATH'` with the directory path where the tick data CSV files are saved (the same directory used in `buffer_main_script.py`).
3. Adjust the `wait_time_seconds` variable if needed. It represents the time to wait (in seconds) between each computation.
4. Save the modifications and run the script.

## Script 3: buffer_plot_script.py

This script reads the most recent computed values CSV file generated by `buffer_compute_values.py` and plots the data using matplotlib. It provides an animated plot that updates every specified interval.

To run this script, follow these steps:

1. Open `buffer_plot_script.py` in a text editor.
2. Locate the line `files = glob.glob("/ADD PATH/computed_FDAX*.csv")` and replace `'/ADD PATH'` with the directory path where the computed values CSV files are saved (the same directory used in `buffer_compute_values.py`).
3. Adjust the `window_size` variable if needed. It represents the number of data points to display in the plot.
4. Save the modifications and run the script.

Note: Make sure to run the scripts in the given order to ensure proper data flow and functionality.

