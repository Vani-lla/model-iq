import itertools

def cycpattern_check(a, b):
    for i in range(len(b)):
        rotated_b = ''.join(itertools.islice(b, i, len(b))) + ''.join(itertools.islice(b, 0, i))
        if rotated_b in a:
            return True
    return False