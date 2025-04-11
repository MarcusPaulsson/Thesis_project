def find_price(A, B):
    for price in range(1, 10001):
        tax_8_percent = (price * 8) // 100
        tax_10_percent = (price * 10) // 100
        if tax_8_percent == A and tax_10_percent == B:
            return price
    return -1

A, B = map(int, input().split())
print(find_price(A, B))