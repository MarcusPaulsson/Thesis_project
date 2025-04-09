from collections import Counter
import math

n = int(input())
divisors = list(map(int, input().split()))

# Count the occurrences of each divisor
counter = Counter(divisors)

# Find the possible candidates for x and y
candidates = list(counter.keys())

# Initialize x and y
x = 1
y = 1

# The highest divisor is the product of the highest factors
for d in candidates:
    if counter[d] == 2:
        # If the divisor appears twice, it must be a common divisor
        x *= d
        y *= d
    else:
        # Otherwise, assign to one of x or y
        if x < y:
            x *= d
        else:
            y *= d

# Print the results
print(x, y)