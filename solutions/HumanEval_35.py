import functools

def max_element(l: list):
    return functools.reduce(lambda a, b: a if a > b else b, l)