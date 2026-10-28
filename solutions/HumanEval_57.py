def monotonic(l: list) -> bool:
    if not l:
        return True
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            decreasing = False
        elif l[i] < l[i - 1]:
            increasing = False
    return increasing or decreasing

# Test cases
assert monotonic([1, 2, 4, 20]) == True
assert monotonic([1, 20, 4, 10]) == False
assert monotonic([4, 1, 0, -10]) == True