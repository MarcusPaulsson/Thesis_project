def find_price(A, B):
    for price in range(1, 10000):  # Arbitrarily large limit for price
        tax_8 = price * 0.08
        tax_10 = price * 0.10
        if int(tax_8) == A and int(tax_10) == B:
            return price
    return -1

A, B = map(int, input().split())
result = find_price(A, B)
print(result)