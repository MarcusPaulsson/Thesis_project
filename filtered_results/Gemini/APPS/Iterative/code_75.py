def solve():
    a, b, c = map(int, input().split())
    
    week = [0, 1, 2, 0, 2, 1, 0]
    
    counts = [week.count(i) for i in range(3)]
    
    min_rations = min(a // counts[0], b // counts[1], c // counts[2])
    
    a -= min_rations * counts[0]
    b -= min_rations * counts[1]
    c -= min_rations * counts[2]
    
    days = min_rations * 7
    
    best_days = days
    
    for start_day in range(7):
        
        temp_days = days
        temp_a, temp_b, temp_c = a, b, c
        
        possible = True
        
        for i in range(7):
            day_of_week = (start_day + i) % 7
            food_type = week[day_of_week]
            
            if food_type == 0:
                if temp_a > 0:
                    temp_a -= 1
                else:
                    possible = False
                    break
            elif food_type == 1:
                if temp_b > 0:
                    temp_b -= 1
                else:
                    possible = False
                    break
            else:
                if temp_c > 0:
                    temp_c -= 1
                else:
                    possible = False
                    break
            
            if possible:
                temp_days += 1
        
        best_days = max(best_days, temp_days)
    
    print(best_days)

solve()