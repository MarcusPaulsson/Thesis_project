def solve():
    n, m, k = map(int, input().split())
    
    low = 1
    high = n * m
    
    while low <= high:
        mid = (low + high) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, m)
        
        if count >= k:
            high = mid - 1
        else:
            low = mid + 1
            
    print(low)

solve()