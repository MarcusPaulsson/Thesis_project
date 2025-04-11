def solve():
    n, m = map(int, input().split())

    low = 0
    high = 2 * 10**9  # Increased upper bound for binary search
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        
        total_sparrows = (mid * (mid + 1)) // 2
        
        barn_level = n + mid * m
        
        if barn_level >= total_sparrows:
            if (n + (mid * m)) % (10**18 + 7) >= total_sparrows % (10**18 + 7):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        else:
            low = mid + 1
            
    
    if ans == -1:
        
        day = 0
        grains = n
        while grains > 0:
            day += 1
            grains = min(n, grains + m)
            grains -= day
        print(day)
    else:
        
        day = 0
        grains = n
        while grains > 0:
            day += 1
            grains = min(n, grains + m)
            grains -= day
        print(day)

solve()