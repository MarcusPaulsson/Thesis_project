from collections import Counter
import sys

def find_x_y(n, divisors):
    count = Counter(divisors)
    common_divisors = [d for d in count if count[d] > 1]
    
    # Calculate x and y
    x = 1
    y = 1
    
    for d in count:
        if count[d] == 1:
            # If the divisor appears once, it belongs to either x or y
            if x % d == 0:
                y *= d
            else:
                x *= d
        else:
            # If the divisor appears twice, it belongs to both x and y
            x *= d
            y *= d
            
    return x, y

# Read input
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Find x and y
x, y = find_x_y(n, divisors)

# Print the result
print(x, y)