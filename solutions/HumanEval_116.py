import functools

@functools.cmp_to_key
def compare(x, y):
    x_bin = bin(x).count('1')
    y_bin = bin(y).count('1')
    if x_bin == y_bin:
        return x - y
    return x_bin - y_bin

def sort_array(arr):
    return sorted(arr, key=compare)