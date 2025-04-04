from collections import Counter
from math import gcd

def find_x_y(n, divisors):
    count = Counter(divisors)
    
    # The largest element in the list must be the maximum of x and y
    max_divisor = max(divisors)
    
    # Get common divisors (those that have a count of 2)
    common_divisors = [d for d in count if count[d] == 2]
    
    # Calculate the potential x and y
    x = 1
    y = 1
    
    for d in divisors:
        if count[d] == 1:
            # If the divisor appears once, assign it to one of x or y
            if x * d <= max_divisor:
                x *= d
            else:
                y *= d
    
    # Now we must include the common divisors
    for d in common_divisors:
        x *= d
        y *= d
    
    return x, y

# Input reading
n = int(input())
divisors = list(map(int, input().split()))

# Find x and y
x, y = find_x_y(n, divisors)

# Output the result
print(x, y)