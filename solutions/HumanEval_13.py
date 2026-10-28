import math


def greatest_common_divisor(a: int, b: int) -> int:
    return math.gcd(a, b)

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5