import numpy as np
import pandas as pd
import utils
import yfinance as yf
import datetime as dt

today = dt.date.today()

end_date = today.strftime('%Y-%m-%d')
start_date = utils.subtract_years(today, 1).strftime('%Y-%m-%d')

tickers = ['AMZN', 'AAPL', 'MSFT', 'GOOG', 'TSLA']

stock_prices = yf.download(tickers, start_date, end_date)['Adj Close']  # historical stock price data

stock_returns = (np.log(stock_prices) - np.log(stock_prices.shift(1))).dropna()
assert len(stock_returns) + 1 == len(stock_prices), "nan values for more than one date have been lost in the returns_df"

pf_weights = np.array([0.13, 0.15, 0.27, 0.18, 0.27])
assert pf_weights.sum() == 1, "Sum of portfolio weights not equal to 1"

pf_returns = (stock_returns * pf_weights).sum(axis=1)
