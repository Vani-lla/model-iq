from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    current_max = float('-inf')
    for number in numbers:
        if number > current_max:
            current_max = number
        rolling_max_list.append(current_max)
    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]