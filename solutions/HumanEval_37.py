def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = sorted([l[i] for i in even_indices])
    result = l.copy()
    for i, value in zip(even_indices, even_values):
        result[i] = value
    return result

# Test cases
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]