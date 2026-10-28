import math

def is_simple_power(x, n):
    if n == 1:
        return x == 1
    return math.isclose(x, n ** round(math.log(x, n)))