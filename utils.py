import datetime
from dateutil.relativedelta import relativedelta


def subtract_years(dte, years):
    """
    Subtracts years from a given date and returns the result.
    :param dte: datetime.date object
    :param years: integer indicating number of years to be subtracted from given date
    :return: resulting date
    """
    assert (isinstance(dte, datetime.date)) or (isinstance(dte, datetime.datetime)),\
        "Ensure date specified is of type 'date' or 'datetime'"
    return dte - relativedelta(years=years)
