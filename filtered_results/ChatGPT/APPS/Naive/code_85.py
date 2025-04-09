def find_price_before_tax(A, B):
    for price in range(1, 10000):  # Arbitrarily high range for price
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.10)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

# Read input
A, B = map(int, input().split())
# Print the result
print(find_price_before_tax(A, B))