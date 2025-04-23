def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [3, 2, 2]  # Number of each food type needed in one week

    # Calculate full weeks that can be sustained
    full_weeks = min(a // food_needed[0], b // food_needed[1], c // food_needed[2])
    
    # Deduct the food used for full weeks
    a -= full_weeks * food_needed[0]
    b -= full_weeks * food_needed[1]
    c -= full_weeks * food_needed[2]

    max_days = full_weeks * 7

    # Try starting from each day of the week
    for start_day in range(7):
        remaining_a, remaining_b, remaining_c = a, b, c
        current_days = 0
        
        for i in range(7):
            day = (start_day + i) % 7
            if day == 0:  # Fish food
                if remaining_a > 0:
                    remaining_a -= 1
                    current_days += 1
                else:
                    break
            elif day == 1:  # Rabbit stew
                if remaining_b > 0:
                    remaining_b -= 1
                    current_days += 1
                else:
                    break
            elif day == 2:  # Chicken stake
                if remaining_c > 0:
                    remaining_c -= 1
                    current_days += 1
                else:
                    break
        
        max_days = max(max_days, full_weeks * 7 + current_days)

    return max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))