import datetime
from dateutil.relativedelta import relativedelta


def subtract_years_from_date(dte: datetime.date, years: int):
    """
    Subtracts years from a given date and returns the result.
    :param dte: datetime.date object
    :param years: integer indicating number of years to be subtracted from given date
    :return: resulting date
    """
    if not (isinstance(dte, datetime.date)) or (isinstance(dte, datetime.datetime)):
        raise TypeError("Ensure dte variable is of type datetime.date or datetime.datetime")
    return dte - relativedelta(years=years)
