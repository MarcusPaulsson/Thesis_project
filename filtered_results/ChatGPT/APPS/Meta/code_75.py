def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 0, 1, 0, 0, 1, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [0, 0, 0]  # fish, rabbit, chicken
    
    # Calculate the total number of complete weeks we can sustain
    complete_weeks = min(a // 3, b // 2, c // 2)
    
    # Update the food supplies after consuming complete weeks
    a -= complete_weeks * 3
    b -= complete_weeks * 2
    c -= complete_weeks * 2
    
    # Total days from complete weeks
    total_days = complete_weeks * 7
    
    # Check for each starting day of the week
    for start_day in range(7):
        days = 0
        current_a, current_b, current_c = a, b, c
        
        # Simulate the days of the week starting from start_day
        for i in range(7):
            day = (start_day + i) % 7
            if day in [0, 3, 6]:  # Fish food days
                if current_a > 0:
                    current_a -= 1
                    days += 1
                else:
                    break
            elif day in [1, 5]:  # Rabbit stew days
                if current_b > 0:
                    current_b -= 1
                    days += 1
                else:
                    break
            else:  # Chicken stake days
                if current_c > 0:
                    current_c -= 1
                    days += 1
                else:
                    break
        
        total_days = max(total_days, complete_weeks * 7 + days)
    
    return total_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))