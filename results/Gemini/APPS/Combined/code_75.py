def solve():
    a, b, c = map(int, input().split())
    
    week = [0, 1, 2, 0, 2, 1, 0]  # 0: fish, 1: rabbit, 2: chicken
    
    weekly_fish = week.count(0)
    weekly_rabbit = week.count(1)
    weekly_chicken = week.count(2)
    
    weekly_days = 7
    
    complete_weeks = min(a // weekly_fish, b // weekly_rabbit, c // weekly_chicken)
    
    a -= complete_weeks * weekly_fish
    b -= complete_weeks * weekly_rabbit
    c -= complete_weeks * weekly_chicken
    
    total_days = complete_weeks * weekly_days
    
    best_days = 0
    
    for start_day in range(7):
        days = 0
        fish = a
        rabbit = b
        chicken = c
        
        current_day = start_day
        
        while True:
            food_type = week[current_day % 7]
            
            if food_type == 0:
                if fish > 0:
                    fish -= 1
                    days += 1
                else:
                    break
            elif food_type == 1:
                if rabbit > 0:
                    rabbit -= 1
                    days += 1
                else:
                    break
            else:
                if chicken > 0:
                    chicken -= 1
                    days += 1
                else:
                    break
            
            current_day += 1
        
        best_days = max(best_days, days)
    
    print(total_days + best_days)

solve()