import collections


def unique(l: list):
    return sorted(collections.Counter(l).keys())
