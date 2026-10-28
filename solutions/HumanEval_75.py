import math

def is_multiply_prime(a):
    if a < 2:
        return False
    prime_factors = []
    for i in range(2, int(math.sqrt(a)) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
    if a > 1:
        prime_factors.append(a)
    return len(prime_factors) == 3 and all(math.isprime(factor) for factor in prime_factors)