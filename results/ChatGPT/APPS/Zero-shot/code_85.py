import sys
import math

def find_price(A, B):
    for price in range(1, 10000):  # Arbitrarily large upper limit for price
        tax_8 = math.floor(price * 0.08)
        tax_10 = math.floor(price * 0.10)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    A, B = map(int, input_data.split())
    result = find_price(A, B)
    print(result)