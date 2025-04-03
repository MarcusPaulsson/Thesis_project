def solve():
    c, m, x = map(int, input().split())
    
    ans = 0
    
    low = 0
    high = min(c, m, x)
    
    while low <= high:
        mid = (low + high) // 2
        
        if c - mid >= 0 and m - mid >= 0 and x - mid >= 0:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
            
    print(ans)

q = int(input())
for _ in range(q):
    solve()