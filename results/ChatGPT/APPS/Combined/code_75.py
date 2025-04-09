def max_days(a, b, c):
    # Daily food requirements based on starting day
    food_schedule = ['fish', 'rabbit', 'chicken', 'fish', 'chicken', 'rabbit', 'fish']
    
    max_days = 0
    
    for start_day in range(7):
        fish_count, rabbit_count, chicken_count = a, b, c
        current_days = 0
        
        # Simulate the first week from the chosen start day
        for day in range(7):
            current_food = food_schedule[(start_day + day) % 7]
            if current_food == 'fish' and fish_count > 0:
                fish_count -= 1
            elif current_food == 'rabbit' and rabbit_count > 0:
                rabbit_count -= 1
            elif current_food == 'chicken' and chicken_count > 0:
                chicken_count -= 1
            else:
                break  # Out of food
            
            current_days += 1
        
        # Calculate full weeks that can be sustained
        full_weeks = min(fish_count // 3, rabbit_count // 2, chicken_count // 2)
        remaining_days = current_days + full_weeks * 7
        
        # Check for additional days after full weeks
        remaining_food = [fish_count - full_weeks * 3, rabbit_count - full_weeks * 2, chicken_count - full_weeks * 2]
        
        for day in range(7):
            current_food = food_schedule[(start_day + current_days + day) % 7]
            if current_food == 'fish' and remaining_food[0] > 0:
                remaining_food[0] -= 1
                remaining_days += 1
            elif current_food == 'rabbit' and remaining_food[1] > 0:
                remaining_food[1] -= 1
                remaining_days += 1
            elif current_food == 'chicken' and remaining_food[2] > 0:
                remaining_food[2] -= 1
                remaining_days += 1
            else:
                break
        
        max_days = max(max_days, remaining_days)
    
    return max_days

# Input reading
a, b, c = map(int, input().split())
# Output the result
print(max_days(a, b, c))