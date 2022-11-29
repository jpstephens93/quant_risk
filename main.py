import numpy
from scipy import stats
import numpy as np
import utils
import yfinance as yf
import datetime as dt

import seaborn as sns
import matplotlib.pyplot as plt

today = dt.date.today()

end_date = today.strftime('%Y-%m-%d')
start_date = utils.subtract_years(today, 1).strftime('%Y-%m-%d')

pf_tickers = ['AMZN', 'AAPL', 'MSFT', 'GOOG', 'TSLA']
bm_ticker = ['SPY']

stock_prices = yf.download(pf_tickers, start_date, end_date)['Adj Close']  # historical stock price data

stock_returns = (np.log(stock_prices) - np.log(stock_prices.shift(1))).dropna()
assert len(stock_returns) + 1 == len(stock_prices), "nan values for more than one date have been lost in the returns_df"

pf_weights = np.array([0.13, 0.15, 0.27, 0.18, 0.27])
assert pf_weights.sum() == 1, "Sum of portfolio weights not equal to 1"

pf_returns = (stock_returns * pf_weights).sum(axis=1)

bm_prices = yf.download(bm_ticker, start_date, end_date)['Adj Close']  # historical benchmark price data
bm_returns = (np.log(bm_prices) - np.log(bm_prices.shift(1))).dropna()

beta, alpha = stats.linregress(bm_returns.values, pf_returns.values)[0:2]

sns.regplot(x=bm_returns.values, y=pf_returns.values)
plt.xlabel("Benchmark Returns")
plt.ylabel("Portfolio Returns")
plt.title("Portfolio Returns vs Benchmark Returns")
plt.show()

# Due to linear nature of equations, if we had beta information for each stock one could simply take the weighted beta
utils.stock_spy_beta(stock_returns.iloc[:, 0])

