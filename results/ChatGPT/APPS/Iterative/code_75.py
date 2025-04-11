def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 0, 1, 0, 0, 1, 0]  # Fish: 0, Rabbit: 1, Chicken: 2
    food_needed = [3, 2, 1]  # Weekly food requirements: Fish, Rabbit, Chicken
    
    # Calculate the total number of complete weeks that can be sustained
    full_weeks = min(a // food_needed[0], b // food_needed[1], c // food_needed[2])
    a -= full_weeks * food_needed[0]
    b -= full_weeks * food_needed[1]
    c -= full_weeks * food_needed[2]
    
    # Calculate the maximum days after full weeks
    max_days = full_weeks * 7
    
    # Try starting from each day of the week
    for start_day in range(7):
        remaining_a, remaining_b, remaining_c = a, b, c
        days = 0
        
        for i in range(7):
            day = (start_day + i) % 7
            if day in [0, 3, 6]:  # Fish food days
                if remaining_a > 0:
                    remaining_a -= 1
                    days += 1
                else:
                    break
            elif day in [1, 5]:  # Rabbit stew days
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
        
        max_days = max(max_days, full_weeks * 7 + days)
    
    return max_days

# Read input
a, b, c = map(int, input().split())
# Output the result
print(max_days(a, b, c))