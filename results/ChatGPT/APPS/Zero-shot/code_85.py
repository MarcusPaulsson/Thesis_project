A, B = map(int, input().split())

def find_lowest_price(A, B):
    for price in range(1, 10000):  # Arbitrary upper limit, can be increased if needed
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.10)
        if tax_8 == A and tax_10 == B:
            return price
    return -1

result = find_lowest_price(A, B)
print(result)