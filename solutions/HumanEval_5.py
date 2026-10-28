from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]