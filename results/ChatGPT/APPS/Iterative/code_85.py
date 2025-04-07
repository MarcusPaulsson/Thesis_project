import sys

def find_price(A, B):
    for price in range(1, 10001):  # Set a reasonable upper limit for search
        tax_8 = price * 0.08 // 1  # Using floor division for clarity
        tax_10 = price * 0.1 // 1
        if tax_8 == A and tax_10 == B:
            return price
    return -1

if __name__ == "__main__":
    A, B = map(int, sys.stdin.read().strip().split())
    if 1 <= A <= B <= 100:
        result = find_price(A, B)
        print(result)
    else:
        print(-1)