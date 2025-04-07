def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    week_pattern = [0, 1, 2, 0, 0, 1, 2]  # 0: fish food, 1: rabbit stew, 2: chicken stake

    # Calculate the number of full weeks we can sustain
    full_weeks = min(a // 3, b // 2, c // 2)
    days = full_weeks * 7

    # Update the remaining food after full weeks
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2

    # Check each day of the week to start and calculate the maximum extra days
    max_extra_days = 0
    for start in range(7):
        remaining_a, remaining_b, remaining_c = a, b, c
        extra_days = 0
        current_day = start

        while True:
            food_type = week_pattern[current_day]
            if food_type == 0 and remaining_a > 0:
                remaining_a -= 1
            elif food_type == 1 and remaining_b > 0:
                remaining_b -= 1
            elif food_type == 2 and remaining_c > 0:
                remaining_c -= 1
            else:
                break
            extra_days += 1
            current_day = (current_day + 1) % 7

        max_extra_days = max(max_extra_days, extra_days)

    return days + max_extra_days

# Read input
a, b, c = map(int, input().split())
# Calculate and print the result
print(max_days(a, b, c))