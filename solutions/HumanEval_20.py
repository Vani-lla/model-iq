from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list to make it easier to find the closest elements
    numbers.sort()

    # Initialize variables to store the closest pair and the smallest difference
    closest_pair = (numbers[0], numbers[1])
    smallest_diff = abs(numbers[1] - numbers[0])

    # Iterate through the sorted list to find the closest pair
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < smallest_diff:
            smallest_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)