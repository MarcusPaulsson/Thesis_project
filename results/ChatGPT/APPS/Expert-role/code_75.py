def max_days(a, b, c):
    week_food = [a, b, c, a, b, c, c]  # Food sequence corresponding to the week
    max_days = 0

    for start_day in range(7):
        food = week_food[:]  # Copy the food list for this starting day
        days = 0
        while True:
            current_day = (start_day + days) % 7
            if food[current_day] > 0:
                food[current_day] -= 1
                days += 1
            else:
                break
        max_days = max(max_days, days)

    full_weeks = min(a // 3, b // 2, c // 2)  # Calculate full weeks of food
    max_days += full_weeks * 7  # Add full weeks to max days

    # Remaining food after full weeks
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2

    # Try to consume the remaining food
    for start_day in range(7):
        food = [a, b, c, a, b, c, c]  # Reset for remaining food
        days = 0
        while True:
            current_day = (start_day + days) % 7
            if food[current_day] > 0:
                food[current_day] -= 1
                days += 1
            else:
                break
        max_days = max(max_days, days)

    return max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))