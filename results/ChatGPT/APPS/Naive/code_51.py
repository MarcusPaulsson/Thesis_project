from collections import Counter
from math import gcd

# Function to find the divisors of a number
def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

# Read input
n = int(input())
divisors_list = list(map(int, input().split()))

# Count the occurrences of each divisor
divisor_count = Counter(divisors_list)

# Find the potential x and y
potential_x = 1
potential_y = 1

# Iterate through the divisors and find x and y
for d in divisor_count:
    if divisor_count[d] == 2:
        # d is a common divisor, multiply it to both x and y
        potential_x *= d
        potential_y *= d
    elif divisor_count[d] == 1:
        # d is a unique divisor, assign it to x or y
        if potential_x < potential_y:
            potential_x *= d
        else:
            potential_y *= d

# Output the results
print(potential_x, potential_y)