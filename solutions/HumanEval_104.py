def unique_digits(x):
    def has_no_even_digit(n):
        return all(int(digit) % 2 != 0 for digit in str(n))

    return sorted(filter(has_no_even_digit, x))