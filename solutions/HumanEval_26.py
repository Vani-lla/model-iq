from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result

# Test case
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]