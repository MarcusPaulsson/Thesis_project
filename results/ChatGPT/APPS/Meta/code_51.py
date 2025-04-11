from collections import Counter
import sys

def find_x_y(n, divisors):
    count = Counter(divisors)
    # The largest number in the list must be either x or y
    max_divisor = max(count)
    
    # Initialize x and y
    x = max_divisor
    y = 1
    
    # Iterate over the divisors to find y
    for d in count:
        if count[d] == 1:  # If d appears only once, it must be a divisor of y
            y *= d
        elif count[d] == 2:  # If d appears twice, it is a divisor of both x and y
            continue
    
    return x, y

# Read input
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Get x and y
x, y = find_x_y(n, divisors)

# Print the result
print(x, y)