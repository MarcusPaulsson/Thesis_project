def max_days(a, b, c):
    # Food consumption pattern based on the day of the week
    food_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    max_days = 0
    
    # Try starting from each day of the week
    for start_day in range(7):
        fish = a
        rabbit = b
        chicken = c
        days = 0
        
        # Simulate the days of the week
        for i in range(7):
            current_day = (start_day + i) % 7
            if food_pattern[current_day] == 0:  # Fish food
                if fish > 0:
                    fish -= 1
                    days += 1
                else:
                    break
            elif food_pattern[current_day] == 1:  # Rabbit stew
                if rabbit > 0:
                    rabbit -= 1
                    days += 1
                else:
                    break
            else:  # Chicken stake
                if chicken > 0:
                    chicken -= 1
                    days += 1
                else:
                    break
        
        # Add full weeks
        full_weeks = min(fish // 3, rabbit // 2, chicken // 2)
        days += full_weeks * 7
        
        # Update maximum days
        max_days = max(max_days, days)
    
    return max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))