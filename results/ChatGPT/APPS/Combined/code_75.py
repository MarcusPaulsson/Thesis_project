def max_days_without_additional_food(a, b, c):
    # Food schedule: Fish (0, 3, 6), Rabbit (1, 5), Chicken (2, 4)
    food_schedule = [a, c, b, c, a, b, a]  # Mon, Tue, Wed, Thu, Fri, Sat, Sun
    max_days = 0

    # Try starting from each day of the week (0 to 6)
    for start_day in range(7):
        remaining_food = food_schedule[:]  # Copy food amounts
        days = 0

        # Simulate days of eating
        while True:
            current_day = (start_day + days) % 7
            if remaining_food[current_day] > 0:
                remaining_food[current_day] -= 1
                days += 1
            else:
                break
        
        max_days = max(max_days, days)

    return max_days

# Read input
a, b, c = map(int, input().split())
# Get the result
result = max_days_without_additional_food(a, b, c)
# Print the result
print(result)