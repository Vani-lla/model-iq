import functools

@functools.lru_cache(maxsize=None)

def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Test cases
assert fib(10) == 55
assert fib(1) == 1
assert fib(8) == 21