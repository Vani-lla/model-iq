import re

def valid_date(date):
    if not date:
        return False

    date_pattern = r'^\d{2}-\d{2}-\d{4}$'
    if not re.match(date_pattern, date):
        return False

    month, day, year = map(int, date.split('-'))

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2 and (day < 1 or day > 29):
        return False

    return True
