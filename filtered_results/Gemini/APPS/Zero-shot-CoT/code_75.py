def solve():
    a, b, c = map(int, input().split())
    
    week = [0, 1, 2, 0, 2, 1, 0]
    
    best_days = 0
    
    for start_day in range(7):
        
        days = 0
        a_temp = a
        b_temp = b
        c_temp = c
        
        current_day = start_day
        
        while True:
            
            food_type = week[current_day % 7]
            
            if food_type == 0:
                if a_temp > 0:
                    a_temp -= 1
                    days += 1
                else:
                    break
            elif food_type == 1:
                if b_temp > 0:
                    b_temp -= 1
                    days += 1
                else:
                    break
            else:
                if c_temp > 0:
                    c_temp -= 1
                    days += 1
                else:
                    break
            
            current_day += 1
        
        best_days = max(best_days, days)
        
    print(best_days)

solve()