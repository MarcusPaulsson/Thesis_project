def solve():
    a, b, c = map(int, input().split())
    
    days = [0] * 7
    days[0] = 0  # Monday
    days[1] = 1  # Tuesday
    days[2] = 2  # Wednesday
    days[3] = 0  # Thursday
    days[4] = 2  # Friday
    days[5] = 1  # Saturday
    days[6] = 0  # Sunday
    
    week_a = 0
    week_b = 0
    week_c = 0
    
    for day in days:
        if day == 0:
            week_a += 1
        elif day == 1:
            week_b += 1
        else:
            week_c += 1
            
    ans = 0
    
    for start_day in range(7):
        cur_a = a
        cur_b = b
        cur_c = c
        
        cur_days = 0
        
        weeks = min(cur_a // week_a, cur_b // week_b, cur_c // week_c)
        cur_days += weeks * 7
        cur_a -= weeks * week_a
        cur_b -= weeks * week_b
        cur_c -= weeks * week_c
        
        temp_days = days[start_day:] + days[:start_day]
        
        for day in temp_days:
            if day == 0:
                if cur_a > 0:
                    cur_a -= 1
                    cur_days += 1
                else:
                    break
            elif day == 1:
                if cur_b > 0:
                    cur_b -= 1
                    cur_days += 1
                else:
                    break
            else:
                if cur_c > 0:
                    cur_c -= 1
                    cur_days += 1
                else:
                    break
        
        ans = max(ans, cur_days)
        
    print(ans)

solve()