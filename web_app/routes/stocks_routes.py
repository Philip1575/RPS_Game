# this is the "web_app/routes/stocks_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.stocks import fetch_stocks_csv, format_usd


stocks_routes = Blueprint("stocks_routes", __name__)


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")


# /stocks/dashboard?symbol=SPOT (GET) or submitted from the stocks form (POST)
@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    print("STOCKS DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args:
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    symbol = (request_data.get("symbol") or "NFLX").strip().upper()

    try:
        df = fetch_stocks_csv(symbol=symbol)
        latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        flash(f"Fetched market data for {symbol}!", "success")
        return render_template("stocks_dashboard.html",
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print("OOPS", err)
        flash(f"Market data error for '{symbol}'. Please check your symbol and try again!", "danger")
        return redirect("/stocks/form")


#
# API ROUTES
#

# /api/stocks.json?symbol=SPOT
@stocks_routes.route("/api/stocks.json")
def stocks_api():
    print("STOCKS DATA (API)...")

    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = (url_params.get("symbol") or "NFLX").strip().upper()

    try:
        df = fetch_stocks_csv(symbol=symbol)
        data = df.to_dict("records")
        return {"symbol": symbol, "data": data}
    except Exception as err:
        print("OOPS", err)
        return {"message": "Market Data Error. Please try again."}, 404
