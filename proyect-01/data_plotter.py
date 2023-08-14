import pandas as pd
import matplotlib.pyplot as plt


def plot_americas_data(data_frame, y_column):
    try:
        # Filtra los datos para incluir solo países de América
        americas_df = data_frame[data_frame["Continent"] == "South America"]
        sorted_df = americas_df.sort_values(by=y_column, ascending=False)

        plt.figure(figsize=(10, 6))
        plt.bar(sorted_df["Country/Territory"], sorted_df[y_column])
        plt.xlabel("Country/Territory")
        plt.ylabel(y_column)
        plt.title(f'Gráfico de {y_column} por país en América')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error:", e)
