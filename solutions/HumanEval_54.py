import collections

def same_chars(s0: str, s1: str) -> bool:
    return collections.Counter(s0) == collections.Counter(s1)