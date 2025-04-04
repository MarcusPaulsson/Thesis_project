def max_days(a, b, c):
    # Food schedule: 0: Fish, 1: Rabbit, 2: Chicken
    food_schedule = [0, 1, 2, 0, 1, 2, 0]  # Monday to Sunday
    
    max_days_possible = 0
    
    for start_day in range(7):
        fish, rabbit, chicken = a, b, c
        days = 0
        
        # Simulate the first week
        for i in range(7):
            day = (start_day + i) % 7
            if food_schedule[day] == 0 and fish > 0:  # Fish food
                fish -= 1
                days += 1
            elif food_schedule[day] == 1 and rabbit > 0:  # Rabbit stew
                rabbit -= 1
                days += 1
            elif food_schedule[day] == 2 and chicken > 0:  # Chicken steak
                chicken -= 1
                days += 1
            else:
                break
        
        # Calculate full weeks that can be sustained
        full_weeks = min(fish // 3, rabbit // 2, chicken // 2)
        if full_weeks > 0:
            days += full_weeks * 7
            fish -= full_weeks * 3
            rabbit -= full_weeks * 2
            chicken -= full_weeks * 2
        
        # Continue for remaining days after full weeks
        for i in range(7):
            day = (start_day + i) % 7
            if food_schedule[day] == 0 and fish > 0:  # Fish food
                fish -= 1
                days += 1
            elif food_schedule[day] == 1 and rabbit > 0:  # Rabbit stew
                rabbit -= 1
                days += 1
            elif food_schedule[day] == 2 and chicken > 0:  # Chicken steak
                chicken -= 1
                days += 1
            else:
                break

        max_days_possible = max(max_days_possible, days)
    
    return max_days_possible

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))