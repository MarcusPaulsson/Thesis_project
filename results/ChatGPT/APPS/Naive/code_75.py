def max_days(a, b, c):
    # Define the food consumption pattern for each day of the week
    food_pattern = [0, 0, 1, 0, 0, 1, 0]  # 0: fish, 1: rabbit, 2: chicken
    food_needed = [2, 1, 1]  # fish, rabbit, chicken
    
    max_days = 0
    
    # Check starting from each day of the week
    for start_day in range(7):
        fish = a
        rabbit = b
        chicken = c
        days = 0
        
        # Simulate the days of the trip
        while True:
            day_of_week = (start_day + days) % 7
            if food_pattern[day_of_week] == 0:  # Fish food
                if fish > 0:
                    fish -= 1
                else:
                    break
            elif food_pattern[day_of_week] == 1:  # Rabbit stew
                if rabbit > 0:
                    rabbit -= 1
                else:
                    break
            else:  # Chicken stake
                if chicken > 0:
                    chicken -= 1
                else:
                    break
            days += 1
        
        max_days = max(max_days, days)
    
    return max_days

# Input reading
a, b, c = map(int, input().split())
print(max_days(a, b, c))