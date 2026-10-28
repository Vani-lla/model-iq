import math

def count_up_to(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in range(2, n) if is_prime(num)]