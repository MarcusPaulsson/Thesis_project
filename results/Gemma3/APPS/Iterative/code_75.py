def solve():
    a, b, c = map(int, input().split())
    
    max_days = 0
    
    for start_day in range(7):
        fish_food = a
        rabbit_stew = b
        chicken_stake = c
        
        days = 0
        
        for day in range(7):
            current_day = (start_day + day) % 7
            
            if current_day in [0, 3, 6]:  # Monday, Thursday, Sunday
                if fish_food > 0:
                    fish_food -= 1
                    days += 1
                else:
                    break
            elif current_day in [1, 5]:  # Tuesday, Saturday
                if rabbit_stew > 0:
                    rabbit_stew -= 1
                    days += 1
                else:
                    break
            else:  # Wednesday, Friday
                if chicken_stake > 0:
                    chicken_stake -= 1
                    days += 1
                else:
                    break
        
        max_days = max(max_days, days)
    
    print(max_days)

solve()