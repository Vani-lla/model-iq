import math


def change_base(x: int, base: int) -> str:
    if base < 2 or base > 9:
        raise ValueError('Base must be between 2 and 9, inclusive.')
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(str(digit) for digit in digits[::-1])
