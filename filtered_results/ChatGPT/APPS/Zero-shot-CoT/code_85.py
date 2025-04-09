import sys
import math

def find_price(A, B):
    for price in range(1, 10000):
        tax_A = math.floor(price * 0.08)
        tax_B = math.floor(price * 0.10)
        if tax_A == A and tax_B == B:
            return price
    return -1

A, B = map(int, sys.stdin.read().strip().split())
result = find_price(A, B)
print(result)