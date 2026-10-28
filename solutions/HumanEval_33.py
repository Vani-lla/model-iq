import math


def sort_third(l: list):
    sorted_indices = [i for i in range(len(l)) if i % 3 == 0]
    sorted_values = sorted(l[i] for i in sorted_indices)
    result = l.copy()
    for i, value in zip(sorted_indices, sorted_values):
        result[i] = value
    return result

# Test cases
assert sort_third([1, 2, 3]) == [1, 2, 3]
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]