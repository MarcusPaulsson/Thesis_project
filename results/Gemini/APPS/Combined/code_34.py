def solve():
    n, a, b = map(int, input().split())
    
    ans = 0
    for i in range(1, n):
        # i plates for cake a, n-i plates for cake b
        if i >= 1 and i < n:
            x = a // i
            y = b // (n - i)
            
            if x > 0 and y > 0:
                ans = max(ans, min(x, y))
            
    print(ans)

solve()