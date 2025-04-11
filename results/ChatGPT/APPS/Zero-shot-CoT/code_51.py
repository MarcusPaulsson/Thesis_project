from collections import Counter
import sys
import math

n = int(input())
divisors = list(map(int, input().split()))

# Count the occurrences of each divisor
count = Counter(divisors)

# Find the maximum divisor
max_divisor = max(count)

# Initialize x and y
x = 1
y = 1

# Calculate x and y based on the divisors
for d in count:
    if count[d] == 1:
        # If the divisor appears once, it belongs to either x or y
        if x * d <= y * d:
            x *= d
        else:
            y *= d
    else:
        # If the divisor appears twice, it belongs to both x and y
        x *= d
        y *= d

# Output the results
print(x, y)