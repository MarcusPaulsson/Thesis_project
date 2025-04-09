from collections import Counter
import sys

def find_x_and_y(divisors):
    divisor_count = Counter(divisors)
    
    # The maximum divisor must be either x or y
    max_divisor = max(divisor_count)
    
    # Find all possible pairs (x, y) using the divisors
    for d in divisor_count:
        if divisor_count[d] == 2:
            # d could be a common divisor
            x = d * (max_divisor // d)
            y = max_divisor
            if all((x % k == 0 or y % k == 0) for k in divisor_count):
                return x, y
    
    # If no common divisor found, return default case
    return max_divisor, max_divisor

# Input reading
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

x, y = find_x_and_y(divisors)
print(x, y)