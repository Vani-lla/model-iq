import collections

def count_distinct_characters(string: str) -> int:
    return len(collections.Counter(string.lower()))
