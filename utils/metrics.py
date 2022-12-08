from scipy import stats
from pandas import Series
from numpy import ndarray, std


def market_beta(portfolio_returns: ndarray, benchmark_returns: ndarray) -> float:
    """
    Calculates the SPY beta for a given stock returns stream.
    :param benchmark_returns: benchmark return stream series
    :param portfolio_returns: stock return stream series
    :return: beta value of type float
    """
    assert len(portfolio_returns) == len(benchmark_returns), "Return streams must be of equal length"
    if isinstance(portfolio_returns, Series):
        portfolio_returns = portfolio_returns.values
    if isinstance(benchmark_returns, Series):
        benchmark_returns = benchmark_returns.values
    return stats.linregress(benchmark_returns, portfolio_returns)[0]


def market_alpha(portfolio_returns: ndarray, benchmark_returns: ndarray) -> float:
    """
    Calculates the SPY beta for a given stock returns stream.
    :param benchmark_returns: benchmark return stream series
    :param portfolio_returns: stock return stream series
    :return: beta value of type float
    """
    assert len(portfolio_returns) == len(benchmark_returns), "Return streams must be of equal length"
    if isinstance(portfolio_returns, Series):
        portfolio_returns = portfolio_returns.values
    if isinstance(benchmark_returns, Series):
        benchmark_returns = benchmark_returns.values
    return stats.linregress(benchmark_returns, portfolio_returns)[1]


def realised_volatility(returns: ndarray):
    if isinstance(returns, Series):
        returns = returns.values
    return std(returns)
