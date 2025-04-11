def solve():
    n, a, b = map(int, input().split())
    
    max_x = 0
    for i in range(1, n):
        if i >= 1 and i < n:
            x1 = a // i
            x2 = b // (n - i)
            
            if x1 > 0 and x2 > 0:
                max_x = max(max_x, min(x1, x2))
    
    print(max_x)

solve()