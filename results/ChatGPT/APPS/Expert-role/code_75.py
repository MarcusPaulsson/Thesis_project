def max_days(a, b, c):
    # Food schedule for each day of the week
    food_schedule = [0, 0, 1, 0, 0, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_count = [a, b, c]
    
    # Calculate full weeks
    full_weeks = min(a // 3, b // 2, c // 1)
    days = full_weeks * 7
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 1
    
    max_extra_days = 0
    
    # Test starting from each day of the week
    for start_day in range(7):
        current_a, current_b, current_c = a, b, c
        extra_days = 0
        
        for day in range(7):  # Only need to check 7 days max
            food_type = food_schedule[(start_day + day) % 7]
            if food_type == 0 and current_a > 0:
                current_a -= 1
                extra_days += 1
            elif food_type == 1 and current_b > 0:
                current_b -= 1
                extra_days += 1
            elif food_type == 2 and current_c > 0:
                current_c -= 1
                extra_days += 1
            else:
                break
        
        max_extra_days = max(max_extra_days, extra_days)
    
    return days + max_extra_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))