def max_days(a, b, c):
    # Define the food consumption pattern for a week
    week_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_count = [a, b, c]
    
    def days_from_starting_day(start):
        food_available = food_count[:]
        days = 0
        
        # Consume food for the first week based on the starting day
        for i in range(7):
            day = (start + i) % 7
            if food_available[week_pattern[day]] > 0:
                food_available[week_pattern[day]] -= 1
                days += 1
            else:
                break
        
        # Calculate how many full weeks can be sustained with the remaining food
        full_weeks = min(food_available[0] // 3, food_available[1] // 2, food_available[2] // 1)
        days += full_weeks * 7
        
        # Update remaining food after full weeks
        food_available[0] -= full_weeks * 3
        food_available[1] -= full_weeks * 2
        food_available[2] -= full_weeks * 1
        
        # Continue to consume food with the remaining supplies
        while True:
            day = (start + days) % 7
            if food_available[week_pattern[day]] > 0:
                food_available[week_pattern[day]] -= 1
                days += 1
            else:
                break
        
        return days

    max_days_count = 0
    for start_day in range(7):
        max_days_count = max(max_days_count, days_from_starting_day(start_day))
    
    return max_days_count

# Input
a, b, c = map(int, input().split())
print(max_days(a, b, c))