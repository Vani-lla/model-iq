import math
def right_angle_triangle(a, b, c):
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)