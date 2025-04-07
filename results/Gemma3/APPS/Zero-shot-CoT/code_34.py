def solve():
    n, a, b = map(int, input().split())
    
    low = 1
    high = min(a, b)
    
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if a // mid + b // mid >= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    print(ans)

solve()