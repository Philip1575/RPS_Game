# this is the "app/stocks.py" file...
# it fetches stock price data from the AlphaVantage API and charts it

import os

from pandas import read_csv
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()  # loads environment variables from the ".env" file

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def format_usd(price):
    """Formats a number as US dollars, like 1234.5678 -> "$1,234.57"."""
    return f"${price:,.2f}"


def fetch_stocks_csv(symbol="NFLX"):
    """Fetches daily stock prices from the AlphaVantage API.

    Params:
        symbol (str) like "NFLX"

    Returns a pandas DataFrame with the time series data.
    """
    request_url = (
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    )
    stocks_df = read_csv(request_url)

    # for an invalid symbol (or a rate limit), the API sends back a message
    # instead of price data, so the expected columns will be missing
    if "adjusted_close" not in stocks_df.columns:
        raise ValueError(f"No price data found for symbol '{symbol}'")

    return stocks_df


def make_stocks_chart(stocks_df, symbol):
    """Creates a line chart of adjusted closing prices over time.

    Params:
        stocks_df (DataFrame) with "timestamp" and "adjusted_close" columns
        symbol (str) like "NFLX", used in the chart title

    Returns a plotly Figure.
    """
    fig = px.line(stocks_df, x="timestamp", y="adjusted_close",
                  title=f"Stock Prices ({symbol})",
                  height=450
                  )
    return fig


if __name__ == "__main__":

    # FETCH THE DATA

    symbol = input("Please choose a stock symbol: ") or "NFLX"

    stocks_df = fetch_stocks_csv(symbol)
    print(stocks_df.head())

    # CHART THE DATA

    fig = make_stocks_chart(stocks_df, symbol)
    fig.show()
