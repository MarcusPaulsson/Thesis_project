def solve():
    n, m = map(int, input().split())
    
    low = 0
    high = 2 * 10**9
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        total_eaten = (mid * (mid + 1)) // 2
        
        if n + mid * m >= total_eaten:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)
    
solve()