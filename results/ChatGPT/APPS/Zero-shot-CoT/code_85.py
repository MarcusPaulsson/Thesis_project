import math
import sys

# Read input
A, B = map(int, sys.stdin.read().strip().split())

# Initialize the result variable to None
result = None

# Check prices from 1 to 1000 (a reasonable range)
for price in range(1, 1001):
    tax_8 = math.floor(price * 0.08)
    tax_10 = math.floor(price * 0.10)
    
    if tax_8 == A and tax_10 == B:
        result = price
        break

# Print the result or -1 if no valid price was found
print(result if result is not None else -1)