import math


def generate_integers(a, b):
    # Ensure a is less than b for the range function
    if a > b:
        a, b = b, a

    # Generate the list of even numbers between a and b
    even_numbers = [num for num in range(a, b + 1) if num % 2 == 0]

    return even_numbers
