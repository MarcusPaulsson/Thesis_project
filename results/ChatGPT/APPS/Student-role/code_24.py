import math

def find_a_b(d):
    # The case when d == 0
    if d == 0:
        return "Y 0.000000000 0.000000000"
    
    # Using the quadratic formula to find the roots of the equation:
    # x^2 - dx + d = 0 -> x = (d ± sqrt(d^2 - 4d)) / 2
    discriminant = d * d - 4 * d
    
    if discriminant < 0:
        return "N"
    
    sqrt_discriminant = math.sqrt(discriminant)
    a = (d + sqrt_discriminant) / 2
    b = (d - sqrt_discriminant) / 2
    
    return f"Y {a:.9f} {b:.9f}"

t = int(input())
for _ in range(t):
    d = int(input())
    print(find_a_b(d))