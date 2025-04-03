def max_days(a, b, c):
    # Define the food schedule for the week
    week_food = ['F', 'R', 'C', 'F', 'C', 'R', 'F']
    
    # Count the number of days for each food type in a week
    week_count = {
        'F': week_food.count('F'),
        'R': week_food.count('R'),
        'C': week_food.count('C')
    }
    
    # Compute maximum full weeks that can be sustained
    full_weeks = min(a // week_count['F'], b // week_count['R'], c // week_count['C'])
    
    # Calculate remaining rations after consuming full weeks
    a -= full_weeks * week_count['F']
    b -= full_weeks * week_count['R']
    c -= full_weeks * week_count['C']
    
    # Start counting days from each day of the week
    max_days = full_weeks * 7
    for start_day in range(7):
        current_a, current_b, current_c = a, b, c
        days = 0
        
        for i in range(7):  # Check up to 7 days
            current_day = (start_day + i) % 7
            food_type = week_food[current_day]
            
            if food_type == 'F' and current_a > 0:
                current_a -= 1
            elif food_type == 'R' and current_b > 0:
                current_b -= 1
            elif food_type == 'C' and current_c > 0:
                current_c -= 1
            else:
                break  # Stop if no food is available
            
            days += 1
        
        max_days = max(max_days, full_weeks * 7 + days)
    
    return max_days

# Read input
a, b, c = map(int, input().split())
# Output the result
print(max_days(a, b, c))