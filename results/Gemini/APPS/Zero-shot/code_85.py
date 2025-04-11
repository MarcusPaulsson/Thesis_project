def solve():
    a, b = map(int, input().split())
    
    ans = -1
    for price in range(1, 2001):
        tax8 = price * 8 // 100
        tax10 = price * 10 // 100
        
        if tax8 == a and tax10 == b:
            ans = price
            break
    
    print(ans)

solve()