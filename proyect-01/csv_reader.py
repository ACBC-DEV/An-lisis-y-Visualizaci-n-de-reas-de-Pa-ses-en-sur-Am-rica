import pandas as pd


def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("Error:", e)
        return None
