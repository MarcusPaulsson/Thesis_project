def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    food_pattern = [0, 0, 1, 0, 0, 1, 2]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [3, 2, 2]  # Full week consumption: fish, rabbit, chicken
    
    # Calculate the maximum full weeks we can sustain
    full_weeks = min(a // food_needed[0], b // food_needed[1], c // food_needed[2])
    a -= full_weeks * food_needed[0]
    b -= full_weeks * food_needed[1]
    c -= full_weeks * food_needed[2]
    
    # Calculate the maximum additional days we can sustain after full weeks
    max_additional_days = 0
    
    for start_day in range(7):
        remaining_a, remaining_b, remaining_c = a, b, c
        days = 0
        
        for i in range(7):
            day = (start_day + i) % 7
            if food_pattern[day] == 0:  # Fish food days
                if remaining_a > 0:
                    remaining_a -= 1
                    days += 1
                else:
                    break
            elif food_pattern[day] == 1:  # Rabbit stew days
                if remaining_b > 0:
                    remaining_b -= 1
                    days += 1
                else:
                    break
            else:  # Chicken stake days
                if remaining_c > 0:
                    remaining_c -= 1
                    days += 1
                else:
                    break
        
        max_additional_days = max(max_additional_days, days)
    
    return full_weeks * 7 + max_additional_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))