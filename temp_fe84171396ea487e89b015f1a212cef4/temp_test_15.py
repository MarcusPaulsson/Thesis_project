def solve():
    a, b, x, y = map(int, input().split())
    
    ans = 0
    
    # Case 1: Window above the dead pixel
    ans = max(ans, a * y)
    
    # Case 2: Window below the dead pixel
    ans = max(ans, a * (b - y - 1))
    
    # Case 3: Window to the left of the dead pixel
    ans = max(ans, b * x)
    
    # Case 4: Window to the right of the dead pixel
    ans = max(ans, b * (a - x - 1))
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()