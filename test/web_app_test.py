# this is the "test/web_app_test.py" file...
# it uses flask's test client to visit pages without running a real server

import pytest
from pandas import DataFrame

from web_app import create_app
import web_app.routes.stocks_routes as stocks_routes


# a small fake dataset, so the web tests don't call the real API
# (the real API is tested once in "test/stocks_test.py", and calling it
# many times in a row can hit the API's rate limit and fail the build)
FAKE_STOCKS_DF = DataFrame({
    "timestamp": ["2026-11-20", "2026-11-19"],
    "open": [100.0, 98.0],
    "high": [102.0, 101.0],
    "low": [99.0, 97.5],
    "close": [101.5, 100.25],
    "adjusted_close": [101.5, 100.25],
    "volume": [1000000, 1200000],
})


def fake_fetch(symbol="NFLX"):
    return FAKE_STOCKS_DF


def fake_fetch_error(symbol="NFLX"):
    raise ValueError(f"No price data found for symbol '{symbol}'")


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_home_routes(client):
    for url in ["/", "/home", "/about"]:
        response = client.get(url)
        assert response.status_code == 200

    response = client.get("/hello?name=Philip")
    assert response.status_code == 200
    assert b"Hello, Philip!" in response.data


def test_rps_form(client):
    response = client.get("/rps/form")
    assert response.status_code == 200
    assert b"<select" in response.data
    assert b"scissors" in response.data


def test_rps_results(client):
    response = client.post("/rps/results", data={"user_choice": "rock"})
    assert response.status_code == 200
    assert any(outcome in response.data for outcome in [b"USER WINS", b"COMPUTER WINS", b"TIE GAME"])


def test_rps_invalid_choice(client):
    response = client.post("/rps/results", data={"user_choice": "lizard"}, follow_redirects=True)
    assert response.request.path == "/rps/form"
    assert b"Please choose rock, paper, or scissors." in response.data


def test_stocks_form(client):
    response = client.get("/stocks/form")
    assert response.status_code == 200
    assert b'name="symbol"' in response.data


def test_stocks_dashboard(client, monkeypatch):
    # swap in the fake data instead of calling the real API
    monkeypatch.setattr(stocks_routes, "fetch_stocks_csv", fake_fetch)

    response = client.post("/stocks/dashboard", data={"symbol": "msft"})
    assert response.status_code == 200
    assert b"MSFT" in response.data
    assert b"$101.50" in response.data  # latest close
    assert b"<table" in response.data
    assert b"chart-container" in response.data


def test_stocks_invalid_symbol(client, monkeypatch):
    # simulate the API having no data for this symbol
    monkeypatch.setattr(stocks_routes, "fetch_stocks_csv", fake_fetch_error)

    response = client.post("/stocks/dashboard", data={"symbol": "NOTAREALSYMBOLXYZ"}, follow_redirects=True)
    assert response.request.path == "/stocks/form"
    assert b"Market data error" in response.data
