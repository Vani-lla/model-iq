import math

def largest_prime_factor(n: int) -> int:
    # Start with the smallest prime number
    largest_factor = 2

    # Divide n by 2 until it's odd
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Check for odd factors from 3 onwards
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        largest_factor = n

    return largest_factor
