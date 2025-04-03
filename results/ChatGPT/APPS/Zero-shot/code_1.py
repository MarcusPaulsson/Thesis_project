from collections import Counter
import math

n = int(input())
divisors = list(map(int, input().split()))

# Count the occurrences of each divisor
count = Counter(divisors)

# Find the LCM of all unique divisors as a candidate for x * y
def lcm(a, b):
    return a * b // math.gcd(a, b)

# Start with the first divisor
x_candidates = []
y_candidates = []

for d in count:
    if count[d] == 2:  # This divisor belongs to both x and y
        x_candidates.append(d)
        y_candidates.append(d)
    elif count[d] == 1:  # This divisor belongs to one of the numbers
        if len(x_candidates) == 0:
            x_candidates.append(d)
        else:
            y_candidates.append(d)

# Calculate x and y
x = 1
for d in x_candidates:
    x *= d

y = 1
for d in y_candidates:
    y *= d

print(x, y)