import numpy as np

def fib4(n: int) -> int:
    if n < 4:
        return [0, 0, 2, 0][n]
    fib4_values = np.zeros(n + 1, dtype=int)
    fib4_values[2] = 2
    for i in range(4, n + 1):
        fib4_values[i] = fib4_values[i - 1] + fib4_values[i - 2] + fib4_values[i - 3] + fib4_values[i - 4]
    return fib4_values[n]