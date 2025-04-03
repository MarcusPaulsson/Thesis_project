A, B = map(int, input().split())

def find_price(A, B):
    for price in range(1, 10000):  # A reasonable upper limit
        tax_8 = price * 8 // 100
        tax_10 = price * 10 // 100
        if tax_8 == A and tax_10 == B:
            return price
    return -1

print(find_price(A, B))