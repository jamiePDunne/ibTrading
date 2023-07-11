# Price Data Downsampling

 contains code for downsampling price data files based on a given threshold. The code is written in Python and utilizes the pandas library for data manipulation and processing.

## Description

The downsampling process involves reducing the number of price data points by aggregating them into larger intervals based on a specified threshold. This can be useful for reducing the size of large datasets or extracting key features from high-frequency data.

The code consists of two main functions:

1. `downsample_file(source_file, dest_file, threshold)`: This function takes a source file containing price data, applies the downsampling algorithm, and saves the downsampled data to a destination file.

2. `downsample_files(source_folder, destination_folder, threshold)`: This function performs the downsampling operation on all CSV files within a source folder, saving the downsampled files to a destination folder. It utilizes the `downsample_file` function internally.

## Usage

To use this code, follow the steps below:

1. Clone this repository to your local machine or download the code files.

2. Make sure you have Python 3.x installed on your system.

3. Install the required dependencies by running the following command:


4. Open the Python script file and locate the section labeled "Example Usage."

5. Edit the `source_folder_path`, `destination_folder_path`, and `threshold_value` variables to specify the appropriate paths and threshold for your use case.

6. Save the changes to the Python script.

7. Open a terminal or command prompt and navigate to the directory containing the Python script.

8. Run the script by executing the following command:


9. The script will process the CSV files in the specified source folder, perform the downsampling operation, and save the downsampled files to the destination folder.

## Logging

The script includes logging functionality to capture important information and potential errors during the downsampling process. The logs are saved to a file named `log.txt` in the destination folder. You can review this log file to monitor the progress and check for any issues encountered during the execution.

## Notes

- Ensure that the source folder contains the CSV files you want to downsample. Only files with the `.csv` extension will be processed.

- The downsampling algorithm is based on comparing consecutive price points with a threshold value. Adjust the `threshold_value` variable in the example usage section to set the desired threshold for downsampling.

- The downsampling process relies on the pandas library for data manipulation and processing. If you haven't installed pandas before, make sure to install it using the provided command in the usage instructions.

## License

This code is provided under the [MIT License](LICENSE).

Feel free to customize and adapt the code to suit your specific requirements.

If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.


