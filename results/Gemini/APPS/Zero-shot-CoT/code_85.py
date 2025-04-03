def solve():
    a, b = map(int, input().split())
    
    for price in range(1, 10**5 + 1):
        tax_8 = int(price * 0.08)
        tax_10 = int(price * 0.10)
        
        if tax_8 == a and tax_10 == b:
            print(price)
            return
    
    print("-1")

solve()