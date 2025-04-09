def max_days_without_purchases(a, b, c):
    # Map the days of the week to food types
    food_schedule = [0, 0, 1, 2, 0, 1, 2, 0]  # 0 -> fish, 1 -> rabbit, 2 -> chicken

    max_days = 0

    # Try starting the trip on each day of the week
    for start_day in range(7):
        fish = a
        rabbit = b
        chicken = c
        days = 0
        current_day = start_day

        while True:
            food_type = food_schedule[current_day]
            if food_type == 0 and fish > 0:
                fish -= 1
            elif food_type == 1 and rabbit > 0:
                rabbit -= 1
            elif food_type == 2 and chicken > 0:
                chicken -= 1
            else:
                break
            
            days += 1
            current_day = (current_day + 1) % 7
        
        max_days = max(max_days, days)

    return max_days

# Input reading
a, b, c = map(int, input().split())
# Output the result
print(max_days_without_purchases(a, b, c))