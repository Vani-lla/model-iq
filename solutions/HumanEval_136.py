import sys


def largest_smallest_integers(lst):
    negative_integers = [x for x in lst if x < 0]
    positive_integers = [x for x in lst if x > 0]

    if not negative_integers:
        a = None
    else:
        a = max(negative_integers)

    if not positive_integers:
        b = None
    else:
        b = min(positive_integers)

    return (a, b)
