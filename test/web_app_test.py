# this is the "test/web_app_test.py" file...
# it uses flask's test client to visit pages without running a real server

import pytest

from web_app import create_app


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


def test_stocks_dashboard(client):
    # this test calls the real AlphaVantage API
    response = client.post("/stocks/dashboard", data={"symbol": "MSFT"})
    assert response.status_code == 200
    assert b"<table" in response.data
    assert b"chart-container" in response.data


def test_stocks_invalid_symbol(client):
    response = client.post("/stocks/dashboard", data={"symbol": "NOTAREALSYMBOLXYZ"}, follow_redirects=True)
    assert response.request.path == "/stocks/form"
    assert b"Market data error" in response.data
