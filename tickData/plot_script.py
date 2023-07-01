import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker


def get_most_recent_csv():
    files = glob.glob("/home/jamie/ib_market_data/computed_FDAX*.csv")
    if files:
        return max(files, key=os.path.getctime)
    else:
        return None


def animate_plot(file_name, window_size):
    fig, ax1 = plt.subplots()  # Create figure and axes for the first plot
    ax2 = ax1.twinx()  # Create a twin axes for the second plot

    def update(frame):
        try:
            df = pd.read_csv(file_name)
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df.set_index('Timestamp', inplace=True)

            # Plot the original data
            ax1.clear()
            ax1.plot(df['Last'], label='Last')
            ax1.plot(df['Bid'], label='Bid')
            ax1.plot(df['Ask'], label='Ask')
            ax1.set_xlabel('Timestamp')
            ax1.set_ylabel('Price')

            # Plot the 'Z' value
            if 'Z' in df.columns and pd.api.types.is_numeric_dtype(df['Z']):
                ax2.clear()
                ax2.plot(df['Z'], label='Z', color='red')
                ax2.set_ylabel('Z Value')

                # Combine the legends from both plots
                lines_1, labels_1 = ax1.get_legend_handles_labels()
                lines_2, labels_2 = ax2.get_legend_handles_labels()
                plt.legend(lines_1 + lines_2, labels_1 + labels_2)

        except FileNotFoundError:
            print(f"File {file_name} not found. Waiting for data...")

    ani = animation.FuncAnimation(fig, update, interval=10000)  # Update every 10 seconds
    plt.show()


if __name__ == '__main__':
    file_name = get_most_recent_csv()
    window_size = 100  # Set the desired window size
    animate_plot(file_name, window_size)
