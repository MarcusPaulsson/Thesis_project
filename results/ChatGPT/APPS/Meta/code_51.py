from collections import Counter
from math import gcd

n = int(input())
divisors = list(map(int, input().split()))

# Count occurrences of each divisor
count = Counter(divisors)

# To find x and y, we need to find the maximum divisor
max_divisor = max(count.keys())
# Start with the assumption that x and y are both the maximum divisor
x = max_divisor
y = max_divisor

# We know that if d is a common divisor, there should be two occurrences of d in the list
for d in count.keys():
    if count[d] == 2:
        continue
    elif count[d] == 1:
        # If a divisor occurs once, it must belong to one of the numbers
        # We can determine the gcd of the two candidates
        if y == max_divisor:
            y = d
        else:
            x = d
    else:
        # If a divisor occurs more than twice (should not happen due to problem constraints)
        pass

# Ensure we print larger first
print(max(x, y), min(x, y))