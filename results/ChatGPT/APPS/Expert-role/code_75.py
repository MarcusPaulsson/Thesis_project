def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 0, 1, 0, 0, 1, 0]  # Fish food on Mon, Thu, Sun; Rabbit stew on Tue, Sat; Chicken stake on Wed
    food_needed = [0, 0, 0]  # [fish, rabbit, chicken]
    
    # Count how many of each food is needed in one week
    for i in range(7):
        if week_pattern[i] == 0:
            food_needed[0] += 1  # Fish food
        elif week_pattern[i] == 1:
            food_needed[1] += 1  # Rabbit stew
        else:
            food_needed[2] += 1  # Chicken stake
    
    # Calculate how many complete weeks can be sustained
    full_weeks = min(a // food_needed[0], b // food_needed[1], c // food_needed[2])
    days = full_weeks * 7
    
    # Remaining food after consuming full weeks
    a -= full_weeks * food_needed[0]
    b -= full_weeks * food_needed[1]
    c -= full_weeks * food_needed[2]
    
    # Check for the maximum additional days possible starting from each day of the week
    max_additional_days = 0
    for start_day in range(7):
        remaining_a, remaining_b, remaining_c = a, b, c
        additional_days = 0
        
        for day in range(7):
            current_day = (start_day + day) % 7
            if current_day in [0, 3, 6]:  # Fish food days
                if remaining_a > 0:
                    remaining_a -= 1
                    additional_days += 1
                else:
                    break
            elif current_day in [1, 5]:  # Rabbit stew days
                if remaining_b > 0:
                    remaining_b -= 1
                    additional_days += 1
                else:
                    break
            else:  # Chicken stake day
                if remaining_c > 0:
                    remaining_c -= 1
                    additional_days += 1
                else:
                    break
        
        max_additional_days = max(max_additional_days, additional_days)
    
    return days + max_additional_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))