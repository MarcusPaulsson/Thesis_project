def solve():
    n, m = map(int, input().split())
    
    left = 1
    right = 2 * 10**9
    
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        total_grain_eaten = mid * (mid + 1) // 2
        
        num_full_days = n // m
        
        if num_full_days > mid:
                total_grain_available = n + mid * m
        else:
            total_grain_available = n + num_full_days * m
                
        
        if total_grain_eaten >= n:
            
            
            total_days_needed = 0
            grain_left = n
            
            curr_day = 1
            while grain_left > 0:
                
                grain_left += m
                grain_left = min(n, grain_left)
                
                grain_left -= curr_day
                curr_day += 1
                
                total_days_needed += 1
                
                if total_days_needed > mid:
                   
                    break
            if grain_left <= 0:
                ans = total_days_needed

        if total_grain_eaten >= n:
                
            days_needed = 0
            grain_left = n
            day_num = 1
            
            while grain_left > 0:
                grain_left = min(n, grain_left + m)
                grain_left -= day_num
                day_num += 1
                days_needed +=1
                
                
            if grain_left <= 0:
                ans = days_needed
                right = mid-1
            else:
                left = mid + 1
                
        else:
            left = mid + 1
            
    print(ans)
    
solve()