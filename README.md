# my-first-app-fall-2026

**Live web app:** https://philip-rps-web-app.onrender.com (hosted on Render's free plan, so the first page load after a period of inactivity can take up to a minute)

## Prerequisites

Install python version 3.x (for example using Anaconda).

## Setup

some instructions here

1. Clone [the repo](https://github.com/s2t2/my-first-app-fall-2026) from GitHub, and put it somewhere (like your Desktop).
2. Navigate to the local repo from the command line (for example if on your desktop):

```sh
cd ~/Desktop/my-first-app-fall-2026
```

3. Create a new Anaconda virtual environment called "rps-env" (first time only):

```sh
conda create -n rps-env python=3.11
```

4. Activate the virtual environment as necessary (every time you come back to the project):

```sh
conda activate rps-env
```

5. Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

The stocks dashboard requires an AlphaVantage API key. Obtain a premium AlphaVantage API key (shared by the professor, or using the [form](https://www.alphavantage.co/support/#api-key)).

Create a local ".env" file in the project's root directory and store your API key in there as an environment variable:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```

The ".env" file is ignored by git (see ".gitignore"), so your API key will not be uploaded to GitHub. Never put your API key directly in a Python file.

For the tests to pass on GitHub Actions, also add your API key as a repository secret: in your GitHub repo, go to Settings > Secrets and variables > Actions > New repository secret, and name it `ALPHAVANTAGE_API_KEY`.

## Usage

some commands here to run our file(s)

Run the example script:

```sh
python app/my_script.py

# alternatively:
python -m app.my_script
```


Run the example script:

```sh
python app/rps.py

# alternatively:
python -m app.rps
```

Run the stocks dashboard (fetches stock prices and opens a chart in your browser):

```sh
python -m app.stocks
```

### Web App

From the project directory, run (works in PowerShell too):

```sh
python -m flask --app web_app run
```

Open http://127.0.0.1:5000 in your browser. Pages include:

  + `/` (home), `/about`, and `/hello?name=Philip`
  + `/rps/form`: choose rock, paper, or scissors from a dropdown, then see the results page
  + `/stocks/form`: enter a stock symbol, then see a dashboard with a chart and a table of recent prices
  + `/api/stocks.json?symbol=MSFT`: the same stock data as JSON

Press Ctrl+C in the terminal to stop the server.

The web app uses flash messages, which need a secret key. Locally a default is used, but you can set your own in the ".env" file:

```sh
SECRET_KEY="some long random value"
```

## Testing

To run tests:

```sh
pytest
```

The tests include the web app pages (see "test/web_app_test.py"). The stocks tests call the real AlphaVantage API, so they need the `ALPHAVANTAGE_API_KEY` (in ".env" locally, or as a repository secret on GitHub Actions).

## Deployment

The app is deployed at https://philip-rps-web-app.onrender.com.

The web app can be deployed to a production server like [Render](https://render.com). Create a new "Web Service" from this GitHub repository with these settings:

  + Build command: `pip install -r requirements.txt`
  + Start command: `gunicorn "web_app:create_app()"`
  + Environment variables: `ALPHAVANTAGE_API_KEY` (your API key) and `SECRET_KEY` (a long random value)
