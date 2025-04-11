from collections import Counter
from math import gcd

n = int(input())
divisors = list(map(int, input().split()))

# Count the occurrences of each divisor
count = Counter(divisors)

# Find the maximum divisor, which should be either x or y
max_divisor = max(count.keys())

# Initialize x and y
x = max_divisor
y = 1

# For each divisor, check if it can be part of y
for d in count:
    if d != max_divisor:
        # If d is a divisor of x, it can also be a divisor of y
        if count[d] == 2:
            y *= d

# Output the results
print(x, y)