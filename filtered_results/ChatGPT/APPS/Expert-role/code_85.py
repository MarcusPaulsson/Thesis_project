import sys
import math

# Read input
A, B = map(int, sys.stdin.read().strip().split())

# Initialize the minimum price found
min_price = -1

# Check all prices from 1 to 1000 (since A and B are <= 100, we can limit the search)
for price in range(1, 1001):
    tax_8 = math.floor(price * 0.08)
    tax_10 = math.floor(price * 0.1)
    
    if tax_8 == A and tax_10 == B:
        if min_price == -1 or price < min_price:
            min_price = price

# Output the result
print(min_price)