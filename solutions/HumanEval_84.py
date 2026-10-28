import math

def solve(N):
    # Convert the number to a string to iterate over each digit
    digits = str(N)
    # Initialize the sum of digits
    sum_of_digits = 0
    # Iterate over each digit and add it to the sum
    for digit in digits:
        sum_of_digits += int(digit)
    # Convert the sum of digits to binary and return it as a string
    return bin(sum_of_digits)[2:]