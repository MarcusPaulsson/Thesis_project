import math

def find_a_b(d):
    if d < 2:
        if d == 0:
            return "Y 0.000000000 0.000000000"
        elif d == 1:
            return "N"
    else:
        # Using the quadratic formula solution for x^2 - dx + d = 0
        discriminant = d ** 2 - 4 * d
        if discriminant < 0:
            return "N"
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            a = (d + sqrt_discriminant) / 2
            b = (d - sqrt_discriminant) / 2
            return f"Y {a:.9f} {b:.9f}"

t = int(input())
for _ in range(t):
    d = int(input())
    print(find_a_b(d))