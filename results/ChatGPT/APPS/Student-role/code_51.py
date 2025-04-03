from collections import Counter
from math import gcd

n = int(input())
divisors = list(map(int, input().split()))

# Count occurrences of each divisor
count = Counter(divisors)

# The two numbers x and y can be found as follows:
# x should be the product of the maximum divisor with the divisor that appears once
# y should be the maximum divisor itself
d1, d2 = 1, 1
for divisor, occurrences in count.items():
    if occurrences == 1:
        d1 = divisor
    elif occurrences == 2:
        d2 = divisor

# The maximum divisor from the list
max_divisor = max(divisors)

# Calculate x and y
x = max_divisor * d1
y = max_divisor * d2

# Output the result
print(x, y)