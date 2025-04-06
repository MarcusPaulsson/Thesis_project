def find_price(A, B):
    for price in range(1, 10000):  # Arbitrarily chosen upper limit
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.10)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

# Input
A, B = map(int, input().split())
# Output
print(find_price(A, B))