import yfinance as yf
import json
from datetime import datetime

# Define parameters
TICKER = "AAPL"
START_DATE = "2025-02-10"
END_DATE = "2026-02-10"
OUTPUT_FILE = "historicalPrices.json"
project_dir = ""

def fetch_close_prices( ticker = TICKER,  start_date = START_DATE, end_date = END_DATE):
  """
  Fetches historical closing price data for the given ticker
  between START_DATE and END_DATE from Yahoo Finance.

  Returns:
      A list of dictionaries containing:
          date (str): date in YYYY-MM-DD format
          close (float): closing price
  """
  df = yf.download(ticker, start=start_date, end=end_date)

  df_close = df['Close']

  def create_dict(row):
    # print(row)
    return {
        "Date": row.name.strftime('%Y-%m-%d'),
        "Close": round(float(row['AAPL']), 10)
    }

  close_dicts = df_close.apply(create_dict, axis=1)

  return close_dicts.tolist()


def save_to_json(data):
  """
  Saves the fetched price data to a JSON file.

  Args:
      data: The list of price dictionaries
      filename: Output filename to write JSON to
  """
  with open(OUTPUT_FILE, 'w') as file:
    json.dump(data, file, indent=4)


if __name__ == "__main__":
    prices = fetch_close_prices()
    save_to_json(prices)
    print("Data successfully saved to historicalPrices.json")