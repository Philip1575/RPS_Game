# this is the "test/stocks_test.py" file...

from pandas import DataFrame

from app.stocks import fetch_stocks_csv, make_stocks_chart


def test_data_fetching():
    stocks_df = fetch_stocks_csv("GOOGL")

    assert isinstance(stocks_df, DataFrame)

    assert "timestamp" in stocks_df.columns
    assert "adjusted_close" in stocks_df.columns

    assert len(stocks_df) >= 100


def test_chart():
    # uses a small fake dataset, so this test doesn't need the API
    stocks_df = DataFrame({
        "timestamp": ["2026-11-13", "2026-11-12", "2026-11-11"],
        "adjusted_close": [101.5, 100.25, 99.0],
    })

    fig = make_stocks_chart(stocks_df, "TEST")

    assert fig.layout.title.text == "Stock Prices (TEST)"
    assert list(fig.data[0].y) == [101.5, 100.25, 99.0]
