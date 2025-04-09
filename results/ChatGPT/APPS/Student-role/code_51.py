from collections import Counter
import sys
import math

n = int(input())
divisors = list(map(int, input().split()))

# Count the occurrences of each divisor
count = Counter(divisors)

# Get the unique divisors
unique_divisors = list(count.keys())

# Initialize x and y
x = 1
y = 1

# Calculate x and y using the count of divisors
for d in unique_divisors:
    if count[d] == 1:
        # d is a divisor of only one of the two numbers
        if x == 1:
            x = d
        else:
            y = d
    elif count[d] == 2:
        # d is a divisor of both numbers
        x *= d
        y *= d

# Adjust x and y if they are not set correctly
if x == 1 and y == 1:
    x = unique_divisors[0]
    y = unique_divisors[1]

print(x, y)