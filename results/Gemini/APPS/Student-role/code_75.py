def solve():
    a, b, c = map(int, input().split())
    
    week = [0, 1, 2, 0, 2, 1, 0] 
    
    best_days = 0
    
    for start_day in range(7):
        
        cur_a, cur_b, cur_c = a, b, c
        cur_days = 0
        
        day = start_day
        
        while True:
            food_type = week[day % 7]
            
            if food_type == 0:
                if cur_a > 0:
                    cur_a -= 1
                    cur_days += 1
                else:
                    break
            elif food_type == 1:
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
            
            day += 1
        
        best_days = max(best_days, cur_days)
        
    print(best_days)

solve()