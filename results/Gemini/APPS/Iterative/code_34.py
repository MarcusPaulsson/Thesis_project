def solve():
    n, a, b = map(int, input().split())
    
    ans = 0
    for i in range(1, n):
        if i < n and (n - i) > 0:
            x = a // i
            y = b // (n - i)
            if x > 0 and y > 0:
                ans = max(ans, min(x, y))
    print(ans)

solve()