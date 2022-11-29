import datetime
from dateutil.relativedelta import relativedelta

import yfinance as yf
import pandas as pd
import numpy as np
from scipy import stats


def subtract_years(dte: datetime.date, years: int):
    """
    Subtracts years from a given date and returns the result.
    :param dte: datetime.date object
    :param years: integer indicating number of years to be subtracted from given date
    :return: resulting date
    """
    if not (isinstance(dte, datetime.date)) or (isinstance(dte, datetime.datetime)):
        raise TypeError("Ensure dte variable is of type datetime.date or datetime.datetime")
    return dte - relativedelta(years=years)


def stock_spy_beta(stock_returns: pd.Series) -> float:
    """
    Calculates the SPY beta for a given stock returns stream.
    :param stock_returns: stock return stream series
    :return: beta value of type float
    """
    if not isinstance(stock_returns, pd.Series):
        raise TypeError("Ensure stock_returns variable is of type pd.Series")
    start_date = min(stock_returns.index).strftime("%Y-%m-%d")
    end_date = max(stock_returns.index).strftime("%Y-%m-%d")
    bm_prices = yf.download('SPY', start_date, end_date)['Adj Close']
    bm_returns = (np.log(bm_prices) - np.log(bm_prices.shift(1))).dropna()
    return stats.linregress(bm_returns.values, stock_returns.values)[0]
