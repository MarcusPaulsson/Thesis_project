def solve():
    n, m = map(int, input().split())

    low = 0
    high = 2 * 10**9 

    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        total_sparrows = (mid * (mid + 1)) // 2
        
        
        full_barns = (total_sparrows - n + m - 1) // m if total_sparrows > n else 0
        
        
        if full_barns < 0:
            full_barns = 0

        
        grains_left = n + full_barns * m - total_sparrows
        
        if grains_left <= 0:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(ans)

solve()