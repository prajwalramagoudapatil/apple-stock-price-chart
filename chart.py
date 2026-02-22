import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os, json
import pandas as pd

INPUT_FILE = "historicalPrices.json"
OUTPUT_IMAGE = "chart.png"

def load_json(file_name = INPUT_FILE):
    """
    Loads historical price data from a JSON file.

    Args:
        filename: Name of the JSON file to read

    Returns:
        A list of dictionaries with date and closing price
    """
    json_data = []

    with open(file_name, 'r') as file:
        json_data = json.load(file)
    return json_data

def create_chart(json_data):
    """
    Creates and saves a line chart of closing stock prices.

    Args:
        data: Price list to plot
        output: Filename of the output image
    """
    df = pd.DataFrame(json_data)

    df['Date'] = pd.to_datetime(df['Date'])

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.plot(df['Date'], df['Close'])

    plt.xlabel('Date')
    plt.ylabel('Close (USD)')
    plt.title('Apple (AAPL) - Historical close prices (last year)')

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE)
    plt.close()



if __name__ == '__main__':
    json_data = load_json()
    create_chart(json_data)
    print('Chart successfully saved as chart.png')

    