import functools

@functools.lru_cache(None)

def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

# Test cases
assert fibfib(1) == 0
assert fibfib(5) == 4
assert fibfib(8) == 24