def solve():
    n, a, b = map(int, input().split())
    
    ans = 0
    for i in range(1, n):
        if i > a or n - i > b:
            continue
        
        x1 = a // i
        x2 = b // (n - i)
        
        ans = max(ans, min(x1, x2))
    
    print(ans)

solve()