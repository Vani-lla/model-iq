import math

def prime_fib(n: int):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

def fib_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

    fib_gen = fib_generator()
    count = 0
    while True:
        fib_num = next(fib_gen)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num

# Test cases
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
