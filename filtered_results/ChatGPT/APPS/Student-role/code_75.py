def max_days(a, b, c):
    # Calculate the maximum full weeks the cat can be fed
    full_weeks = min(a // 3, b // 2, c // 2)
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2
    
    # Calculate the remaining days the cat can be fed starting from each day of the week
    max_days = 0
    for start_day in range(7):
        days = 0
        remaining_a, remaining_b, remaining_c = a, b, c
        
        for day in range(7):
            current_day = (start_day + day) % 7
            if current_day in [0, 3, 6]:  # Fish food days
                if remaining_a > 0:
                    remaining_a -= 1
                    days += 1
                else:
                    break
            elif current_day in [1, 5]:  # Rabbit stew days
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
        
        max_days = max(max_days, days)
    
    return full_weeks * 7 + max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))