def max_days(a, b, c):
    # Define the weekly food consumption pattern
    week_pattern = ['fish', 'rabbit', 'chicken', 'fish', 'chicken', 'rabbit', 'fish']
    
    # Map the food types to their available rations
    food_map = {'fish': a, 'rabbit': b, 'chicken': c}
    
    max_days = 0
    
    # Try starting on each day of the week
    for start_day in range(7):
        current_food = food_map.copy()
        days = 0
        
        # Simulate the days
        for i in range(7):  # A maximum of 7 days in a week
            day = (start_day + i) % 7
            food_type = week_pattern[day]
            
            if current_food[food_type] > 0:
                current_food[food_type] -= 1
                days += 1
            else:
                break
        
        max_days = max(max_days, days)
    
    return max_days

# Input reading
a, b, c = map(int, input().split())
# Output the maximum number of days
print(max_days(a, b, c))