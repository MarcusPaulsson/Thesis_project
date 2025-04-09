def solve():
    n, a, b = map(int, input().split())
    
    ans = 0
    for i in range(1, n):
        plates_a = i
        plates_b = n - i
        
        if plates_a > 0 and plates_b > 0:
            x = a // plates_a
            y = b // plates_b
            ans = max(ans, min(x, y))
            
    print(ans)

solve()