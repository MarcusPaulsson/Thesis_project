def max_days(a, b, c):
    # Calculate the maximum full weeks that can be fed
    full_weeks = min(a // 3, b // 2, c // 2)
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2
    
    max_days = full_weeks * 7
    
    # Check each starting day of the week
    for start_day in range(7):
        days = 0
        food = [a, b, c]
        week_pattern = [0, 0, 1, 0, 0, 1, 0]  # 0: fish, 1: rabbit, 2: chicken
        
        for i in range(7):
            day = (start_day + i) % 7
            if day in (0, 3, 6):  # Fish days
                if food[0] > 0:
                    food[0] -= 1
                    days += 1
                else:
                    break
            elif day in (1, 5):  # Rabbit days
                if food[1] > 0:
                    food[1] -= 1
                    days += 1
                else:
                    break
            else:  # Chicken days
                if food[2] > 0:
                    food[2] -= 1
                    days += 1
                else:
                    break
        
        max_days = max(max_days, days)
    
    return max_days

# Read input
a, b, c = map(int, input().split())
# Print output
print(max_days(a, b, c))