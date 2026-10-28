from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    # Start with the smallest prime number
    divisor = 2
    while n >= divisor:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

# Test cases
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]