def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [3, 2, 2]  # Total food needed for one week
    
    # Calculate how many full weeks can be sustained
    full_weeks = min(a // food_needed[0], b // food_needed[1], c // food_needed[2])
    
    # Reduce the food supplies by the amount used in full weeks
    a -= full_weeks * food_needed[0]
    b -= full_weeks * food_needed[1]
    c -= full_weeks * food_needed[2]
    
    # Total days from full weeks
    max_days = full_weeks * 7
    
    # Check for each starting day of the week
    for start_day in range(7):
        days = 0
        a_temp, b_temp, c_temp = a, b, c
        
        # Simulate the days of the week starting from start_day
        for i in range(7):
            current_day = (start_day + i) % 7
            if week_pattern[current_day] == 0 and a_temp > 0:
                a_temp -= 1
                days += 1
            elif week_pattern[current_day] == 1 and b_temp > 0:
                b_temp -= 1
                days += 1
            elif week_pattern[current_day] == 2 and c_temp > 0:
                c_temp -= 1
                days += 1
            else:
                break  # No food available for the current day, stop counting
        
        max_days = max(max_days, days)
    
    return max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))