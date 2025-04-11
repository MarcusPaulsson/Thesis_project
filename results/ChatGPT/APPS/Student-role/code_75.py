def max_days(a, b, c):
    # Calculate full weeks
    full_weeks = min(a // 3, b // 2, c // 2)
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2
    days = full_weeks * 7

    # Try starting from each day of the week
    for start_day in range(7):
        current_a, current_b, current_c = a, b, c
        current_days = 0
        
        for day in range(7):
            food_type = (start_day + day) % 7
            if food_type in [0, 3, 6]:  # Fish food days
                if current_a > 0:
                    current_a -= 1
                    current_days += 1
                else:
                    break
            elif food_type in [1, 5]:  # Rabbit stew days
                if current_b > 0:
                    current_b -= 1
                    current_days += 1
                else:
                    break
            else:  # Chicken stake days
                if current_c > 0:
                    current_c -= 1
                    current_days += 1
                else:
                    break

        days = max(days, current_days + full_weeks * 7)

    return days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))