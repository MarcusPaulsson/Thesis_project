from collections import Counter
from math import gcd

n = int(input())
divisors = list(map(int, input().split()))

# Count the occurrences of each divisor
count = Counter(divisors)

# Get all unique divisors
unique_divisors = list(count.keys())

# The product x * y is the product of all unique divisors raised to their counts
x = 1
y = 1

# For each unique divisor
for d in unique_divisors:
    # If the count is 2, it is a common divisor
    if count[d] == 2:
        x *= d
        y *= d
    # If the count is 1, assign it to x or y
    elif count[d] == 1:
        if x < y:
            x *= d
        else:
            y *= d

print(x, y)