import sys
import math

A, B = map(int, sys.stdin.read().strip().split())

def find_price(A, B):
    for price in range(1, 10000):  # Set a reasonable upper limit
        tax_8 = math.floor(price * 0.08)
        tax_10 = math.floor(price * 0.10)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

result = find_price(A, B)
print(result)