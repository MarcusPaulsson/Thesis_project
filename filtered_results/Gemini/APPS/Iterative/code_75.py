def solve():
    a, b, c = map(int, input().split())
    
    week = [0, 1, 2, 0, 2, 1, 0]
    
    week_a = week.count(0)
    week_b = week.count(1)
    week_c = week.count(2)
    
    min_weeks = min(a // week_a, b // week_b, c // week_c)
    
    a -= min_weeks * week_a
    b -= min_weeks * week_b
    c -= min_weeks * week_c
    
    ans = min_weeks * 7
    
    max_days = 0
    
    for start_day in range(7):
        temp_a, temp_b, temp_c = a, b, c
        days = 0
        
        for i in range(7):
            current_day = (start_day + i) % 7
            
            if week[current_day] == 0:
                if temp_a > 0:
                    temp_a -= 1
                    days += 1
                else:
                    break
            elif week[current_day] == 1:
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
        
        max_days = max(max_days, days)
    
    print(ans + max_days)

solve()