import math

def find_numbers(d):
    if d == 0:
        return "Y 0.000000000 0.000000000"
    elif d == 1:
        return "N"
    
    # Calculate the discriminant
    discriminant = d**2 - 4 * d
    if discriminant < 0:
        return "N"
    
    # Calculate the two possible solutions
    sqrt_discriminant = math.sqrt(discriminant)
    a = (d + sqrt_discriminant) / 2
    b = (d - sqrt_discriminant) / 2
    
    return f"Y {a:.9f} {b:.9f}"

t = int(input())
for _ in range(t):
    d = int(input())
    result = find_numbers(d)
    print(result)