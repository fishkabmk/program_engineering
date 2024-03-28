import math


one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

a_max, a_min = max(one), min(one)
b_max, b_min = max(two), min(two)
c_max, c_min = max(three), min(three)

p_max = (a_max + b_max + c_max) / 2
s_max = math.sqrt(p_max * (p_max - a_max) * (p_max - b_max) * (p_max - c_max))

p_min = (a_min + b_min + c_min) / 2
s_min = math.sqrt(p_min * (p_min - a_min) * (p_min - b_min) * (p_min - c_min))

print(f"Площадь большого треугольника: {s_max:.2f}")
print(f"Площадь маленького треугольника: {s_min:.2f}")
