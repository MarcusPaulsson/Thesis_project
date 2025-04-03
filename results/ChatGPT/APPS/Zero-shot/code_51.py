from collections import Counter
import sys

n = int(input().strip())
divisors = list(map(int, input().strip().split()))

# Count the occurrences of each divisor
count = Counter(divisors)

# Initialize x and y
x, y = 1, 1

# For each divisor, if it appears twice, it is a common divisor
for d in count:
    if count[d] == 2:
        # If d appears twice, it is a divisor for both x and y
        x *= d
        y *= d
    elif count[d] == 1:
        # If d appears once, assign it to either x or y
        if x < y:
            x *= d
        else:
            y *= d

print(x, y)