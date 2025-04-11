def max_days_without_purchases(a, b, c):
    # Define the food consumption pattern for each day of the week
    food_pattern = ['fish', 'rabbit', 'chicken', 'fish', 'chicken', 'rabbit', 'fish']
    
    # Calculate the maximum number of complete weeks that can be sustained
    complete_weeks = min(a // 3, b // 2, c // 2)
    
    # Deduct the food consumed in complete weeks
    a -= complete_weeks * 3
    b -= complete_weeks * 2
    c -= complete_weeks * 2
    
    # Total days from complete weeks
    max_days = complete_weeks * 7
    
    # Check starting from each day of the week
    for start_day in range(7):
        days = 0
        a_temp, b_temp, c_temp = a, b, c
        
        # Simulate the days of the week starting from start_day
        for i in range(7):
            current_day = (start_day + i) % 7
            if food_pattern[current_day] == 'fish' and a_temp > 0:
                a_temp -= 1
                days += 1
            elif food_pattern[current_day] == 'rabbit' and b_temp > 0:
                b_temp -= 1
                days += 1
            elif food_pattern[current_day] == 'chicken' and c_temp > 0:
                c_temp -= 1
                days += 1
            else:
                break
        
        max_days = max(max_days, days)
    
    return max_days

# Input reading
a, b, c = map(int, input().split())
# Output the result
print(max_days_without_purchases(a, b, c))