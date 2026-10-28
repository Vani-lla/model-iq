import typing


def add(lst: typing.List[int]) -> int:
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0)
