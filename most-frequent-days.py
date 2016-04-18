from datetime import date
from calendar import isleap


def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    if isleap(year):
        return [i.strftime('%A') for i in
                sorted([date(year, 1, 1),
                        date(year, 1, 2)],
                       key=lambda x: x.weekday())]
    else:
        return [date(year, 1, 1).strftime('%A')]
