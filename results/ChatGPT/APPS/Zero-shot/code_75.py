def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [3] * 7  # To track how many days can be sustained
    
    # Calculate the maximum full weeks that can be sustained
    full_weeks = min(a // 3, b // 2, c // 1)
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 1
    
    # Start checking from each day of the week
    max_days_count = full_weeks * 7
    
    for start_day in range(7):
        days_count = 0
        a_temp, b_temp, c_temp = a, b, c
        
        for i in range(7):
            current_day = (start_day + i) % 7
            if week_pattern[current_day] == 0:  # fish food
                if a_temp > 0:
                    a_temp -= 1
                    days_count += 1
                else:
                    break
            elif week_pattern[current_day] == 1:  # rabbit stew
                if b_temp > 0:
                    b_temp -= 1
                    days_count += 1
                else:
                    break
            elif week_pattern[current_day] == 2:  # chicken stake
                if c_temp > 0:
                    c_temp -= 1
                    days_count += 1
                else:
                    break
        
        max_days_count = max(max_days_count, full_weeks * 7 + days_count)
    
    return max_days_count

# Read input
a, b, c = map(int, input().split())
# Print the result
print(max_days(a, b, c))