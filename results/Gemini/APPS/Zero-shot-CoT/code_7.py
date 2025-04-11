def solve():
    n, m = map(int, input().split())

    l, r = 0, 2 * 10**9
    ans = r

    while l <= r:
        mid = (l + r) // 2
        
        total_sparrows = mid * (mid + 1) // 2
        
        if total_sparrows >= n:
            
            low = 0
            high = mid
            
            first_day = mid
            
            while low <= high:
                mid2 = (low + high) // 2
                
                grains_after_sparrows = n
                
                num_full_days = mid2
                
                grains_after_sparrows += num_full_days * m
                
                sparrows_eaten = mid2 * (mid2 + 1) // 2
                
                grains_after_sparrows -= sparrows_eaten
                
                if grains_after_sparrows <= 0:
                    first_day = mid2
                    high = mid2 - 1
                else:
                    low = mid2 + 1
            
            
            grains_after_sparrows = n
            
            num_full_days = first_day
            
            grains_after_sparrows += num_full_days * m
            
            sparrows_eaten = first_day * (first_day + 1) // 2
            
            grains_after_sparrows -= sparrows_eaten
            
            if grains_after_sparrows <= 0:
                ans = first_day
                r = mid - 1
            else:
                l = mid + 1
        else:
            l = mid + 1

    print(ans)

solve()