def solve():
    a, b, c = map(int, input().split())
    
    weekly_schedule = [0, 1, 2, 0, 2, 1, 0] 
    
    best_days = 0
    
    for start_day in range(7):
        days = 0
        temp_a = a
        temp_b = b
        temp_c = c
        
        current_day = start_day
        
        while True:
            food_type = weekly_schedule[current_day % 7]
            
            if food_type == 0:
                if temp_a > 0:
                    temp_a -= 1
                    days += 1
                else:
                    break
            elif food_type == 1:
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
            
            current_day += 1
        
        best_days = max(best_days, days)
    
    print(best_days)

solve()