from collections import Counter
import sys

def find_x_y(divisors):
    count = Counter(divisors)
    unique_divisors = list(count.keys())
    
    # Initialize x and y
    x = 1
    y = 1
    
    # Calculate x and y based on the counts of divisors
    for d in unique_divisors:
        if count[d] == 2:
            x *= d
            y *= d
        elif count[d] == 1:
            x *= d
    
    return x, y

n = int(input().strip())
divisors = list(map(int, input().strip().split()))

x, y = find_x_y(divisors)
print(x, y)