import math

def min_perimeter(a, b):
    # Find the greatest common divisor of a and b
    gcd = math.gcd(a, b)
    
    # Calculate the dimensions of the rectangle
    length = a // gcd + b // gcd
    width = gcd
    
    # Calculate the perimeter of the rectangle
    perimeter = 2 * (length + width)
    
    return perimeter

# Read input
a, b = map(int, input().split())

# Print output
print(min_perimeter(a, b))