import math


def calc_triangle(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {s:.2f}")
