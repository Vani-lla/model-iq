from typing import List


def string_xor(a: str, b: str) -> str:
    return ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(a, b))
