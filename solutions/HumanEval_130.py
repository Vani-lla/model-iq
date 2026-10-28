def tri(n):
    if n == 1:
        return [3]
    tribonacci = [3]
    for i in range(1, n):
        if i % 2 == 0:
            tribonacci.append(1 + i / 2)
        else:
            tribonacci.append(tribonacci[-1] + tribonacci[-2] + tribonacci[-3])
    return tribonacci