def max_days(a, b, c):
    # Days of the week food types
    food_schedule = [0, 0, 1, 2, 0, 1, 2, 0]  # 0: fish, 1: rabbit, 2: chicken
    max_days = 0

    # Simulate starting from each day of the week
    for start_day in range(7):
        fish = a
        rabbit = b
        chicken = c
        days = 0
        
        # Continue eating until we run out of food
        while True:
            current_food = food_schedule[(start_day + days) % 7]
            if current_food == 0:
                if fish > 0:
                    fish -= 1
                else:
                    break
            elif current_food == 1:
                if rabbit > 0:
                    rabbit -= 1
                else:
                    break
            else:  # current_food == 2
                if chicken > 0:
                    chicken -= 1
                else:
                    break
            days += 1
        
        max_days = max(max_days, days)

    return max_days

# Read input
a, b, c = map(int, input().split())
# Output the result
print(max_days(a, b, c))