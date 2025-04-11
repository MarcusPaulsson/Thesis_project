def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [3, 2, 2]  # Number of each type of food needed in a week

    # Calculate the maximum full weeks we can sustain
    full_weeks = min(a // food_needed[0], b // food_needed[1], c // food_needed[2])
    a -= full_weeks * food_needed[0]
    b -= full_weeks * food_needed[1]
    c -= full_weeks * food_needed[2]
    
    max_days = full_weeks * 7

    # Try starting from each day of the week
    for start_day in range(7):
        remaining_a, remaining_b, remaining_c = a, b, c
        days = 0
        for i in range(7):
            day = (start_day + i) % 7
            if week_pattern[day] == 0 and remaining_a > 0:
                remaining_a -= 1
                days += 1
            elif week_pattern[day] == 1 and remaining_b > 0:
                remaining_b -= 1
                days += 1
            elif week_pattern[day] == 2 and remaining_c > 0:
                remaining_c -= 1
                days += 1
            else:
                break
        max_days = max(max_days, full_weeks * 7 + days)

    return max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))