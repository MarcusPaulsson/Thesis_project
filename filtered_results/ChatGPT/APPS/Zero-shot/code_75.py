def max_days(a, b, c):
    # Food consumption pattern for each day of the week
    week_pattern = [0, 0, 1, 0, 0, 1, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [0, 0, 0]  # fish, rabbit, chicken
    
    # Calculate the maximum full weeks we can sustain
    full_weeks = min(a // 3, b // 2, c // 2)
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2
    
    max_days = full_weeks * 7
    
    # Try starting from each day of the week
    for start_day in range(7):
        days = 0
        remaining_a, remaining_b, remaining_c = a, b, c
        
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

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))