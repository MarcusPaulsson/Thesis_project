from collections import Counter
from math import gcd
from functools import reduce

n = int(input())
divisors = list(map(int, input().split()))

# Count the frequency of each divisor
count = Counter(divisors)

# Find the maximum divisor, which should be x or y
max_divisor = max(count.keys())

# To find x and y, we will iterate over the divisors and determine their possible pairs
# We can calculate x and y by multiplying all unique divisors
x = 1
y = 1

# Separate common and non-common divisors
for d in count:
    if count[d] > 1:
        # This is a common divisor, multiply it to both x and y
        x *= d
        y *= d
    else:
        # This is a non-common divisor, assign it to x or y based on their current products
        if x < y:
            x *= d
        else:
            y *= d

print(x, y)