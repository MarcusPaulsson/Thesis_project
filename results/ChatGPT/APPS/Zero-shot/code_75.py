def max_days(a, b, c):
    # Days of the week food schedule
    week_food = [a, b, c, a, c, b, a]  # fish, rabbit, chicken respectively
    
    # Calculate how many complete weeks can be sustained
    complete_weeks = min(a // 3, b // 2, c // 1)
    a -= complete_weeks * 3
    b -= complete_weeks * 2
    c -= complete_weeks * 1
    
    # Now check for how many additional days we can go
    max_additional_days = 0
    
    # Try starting from each day of the week
    for start_day in range(7):
        food = [a, b, c]
        days = 0
        
        # Simulate days
        for i in range(7):
            day = (start_day + i) % 7
            if food[day // 2] > 0:  # fish food for 0, 3, 6 | rabbit for 1, 5 | chicken for 2, 4
                food[day // 2] -= 1
                days += 1
            else:
                break
        
        max_additional_days = max(max_additional_days, days)
    
    return complete_weeks * 7 + max_additional_days

# Input
a, b, c = map(int, input().split())
print(max_days(a, b, c))