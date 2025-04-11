import sys
import math

def find_price(A, B):
    for price in range(1, 10000):  # Arbitrary upper limit for price search
        tax_8 = math.floor(price * 0.08)
        tax_10 = math.floor(price * 0.10)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

if __name__ == "__main__":
    A, B = map(int, sys.stdin.read().strip().split())
    result = find_price(A, B)
    print(result)