import sys
import math

def find_price(A, B):
    for price in range(1, 10000):  # Arbitrarily chosen upper limit for price
        tax_8 = math.floor(price * 0.08)
        tax_10 = math.floor(price * 0.10)
        
        if tax_8 == A and tax_10 == B:
            return price
    return -1

if __name__ == "__main__":
    A, B = map(int, sys.stdin.read().strip().split())
    if 1 <= A <= B <= 100:  # Validate input constraints
        result = find_price(A, B)
        print(result)
    else:
        print(-1)  # Print -1 if input constraints are not met