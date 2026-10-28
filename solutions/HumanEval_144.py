import fractions

def simplify(x, n):
    x_fraction = fractions.Fraction(x)
    n_fraction = fractions.Fraction(n)
    result = x_fraction * n_fraction
    return result.denominator == 1