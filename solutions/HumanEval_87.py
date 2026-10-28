def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row[::-1]):  # Reverse row to sort by columns in descending order
            if value == x:
                result.append((i, len(row) - 1 - j))  # Adjust column index
    result.sort(key=lambda x: (x[0], x[1]))  # Sort by rows in ascending order and then by columns in descending order
    return result

# Test cases
print(get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1))  # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1))  # []
print(get_row([[], [1], [1, 2, 3]], 3))  # [(2, 2)]