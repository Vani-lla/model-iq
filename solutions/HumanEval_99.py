import math

def closest_integer(value):
    number = float(value)
    if number > 0:
        return math.floor(number + 0.5)
    else:
        return math.ceil(number - 0.5)