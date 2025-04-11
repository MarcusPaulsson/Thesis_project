def solve():
    a, b, c = map(int, input().split())
    
    week = [0, 1, 2, 0, 2, 1, 0]
    
    min_weeks = min(a // 3, b // 2, c // 2)
    
    a -= min_weeks * 3
    b -= min_weeks * 2
    c -= min_weeks * 2
    
    ans = min_weeks * 7
    
    max_days = 0
    
    for start_day in range(7):
        temp_a, temp_b, temp_c = a, b, c
        days = 0
        curr_day = start_day
        
        while True:
            food = week[curr_day % 7]
            
            if food == 0:
                if temp_a > 0:
                    temp_a -= 1
                    days += 1
                else:
                    break
            elif food == 1:
                if temp_b > 0:
                    temp_b -= 1
                    days += 1
                else:
                    break
            else:
                if temp_c > 0:
                    temp_c -= 1
                    days += 1
                else:
                    break
            
            curr_day += 1
        
        max_days = max(max_days, days)
    
    print(ans + max_days)

solve()