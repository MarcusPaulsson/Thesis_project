def solve():
    n, a, b = map(int, input().split())
    
    ans = 0
    for i in range(1, n):
        if i >= a or n - i >= b:
            continue
        
        x = a // i
        y = b // (n - i)
        
        ans = max(ans, min(x, y))
    
    print(ans)

solve()