import math


def poly(xs: list, x: float):
    """Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n"""
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution."""
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("Invalid input: xs must have even number of coefficients and largest non zero coefficient")

    # Use Newton's method to find a zero
    x = 0.0
    while True:
        fx = poly(xs, x)
        fpx = sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs) if i > 0])
        if abs(fx) < 1e-6:
            return round(x, 2)
        x -= fx / fpx
