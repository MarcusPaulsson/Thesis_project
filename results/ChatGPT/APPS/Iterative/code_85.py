def find_price(A, B):
    for price in range(1, 10000):  # Arbitrarily chosen upper limit
        tax_8 = price * 0.08  # Consumption tax at 8%
        tax_10 = price * 0.10  # Consumption tax at 10%
        if int(tax_8) == A and int(tax_10) == B:
            return price
    return -1

# Input reading
A, B = map(int, input().split())
result = find_price(A, B)
print(result)