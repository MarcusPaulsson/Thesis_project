from collections import Counter
import sys

def find_x_y(divisors):
    count = Counter(divisors)
    
    # The maximum divisor is either x or y
    x = max(divisors)
    # Start with x and find y
    y = 1
    
    for d in count:
        if d == x:
            continue
        # For each divisor d, we check if it can be part of y
        if count[d] == 1:
            y *= d
    
    return x, y

# Input reading
n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Finding x and y
x, y = find_x_y(divisors)

# Output
print(x, y)