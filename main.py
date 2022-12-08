from utils import metrics, misc

import numpy as np
import yfinance as yf
import datetime as dt

import seaborn as sns
import matplotlib.pyplot as plt

today = dt.date.today()

end_date = today.strftime('%Y-%m-%d')
start_date = misc.subtract_years_from_date(today, 1).strftime('%Y-%m-%d')

pf_tickers = ['AMZN', 'AAPL', 'MSFT', 'GOOG', 'TSLA']
bm_ticker = ['SPY']

stock_prices = yf.download(pf_tickers, start_date, end_date)['Adj Close']  # historical stock price data

stock_returns = (np.log(stock_prices) - np.log(stock_prices.shift(1))).dropna()

pf_weights = np.array([0.13, 0.15, 0.27, 0.18, 0.27])

bm_prices = yf.download(bm_ticker, start_date, end_date)['Adj Close']  # historical benchmark price data

pf_returns = (stock_returns * pf_weights).sum(axis=1)

bm_returns = (np.log(bm_prices) - np.log(bm_prices.shift(1))).dropna()

pf_beta = metrics.market_beta(pf_returns.values, bm_returns)

pf_alpha = metrics.market_alpha(pf_returns.values, bm_returns)

sns.regplot(x=bm_returns.values, y=pf_returns.values)
plt.xlabel("Benchmark Returns")
plt.ylabel("Portfolio Returns")
plt.title("Portfolio Returns vs Benchmark Returns")
plt.show()

# Due to linear nature of equations, if we had beta information for each stock one could simply take the weighted beta
metrics.market_beta(stock_returns.iloc[:, 0])

