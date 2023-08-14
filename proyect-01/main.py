import pandas as pd
import matplotlib.pyplot as plt
from csv_reader import read_csv_file
from data_plotter import plot_americas_data


def main():
    file_path = "data.csv"
    data_frame = read_csv_file(file_path)

    if data_frame is not None:
        y_column = "Area (km²)"
        plot_americas_data(data_frame, y_column)


if __name__ == "__main__":
    main()
