def max_days(a, b, c):
    # Food consumption pattern based on the day of the week
    food_pattern = [1, 1, 0, 1, 0, 1, 0]  # Fish: 1, Rabbit: 1, Chicken: 0
    max_days = 0

    # Check each starting day of the week
    for start_day in range(7):
        # Copy the original food supplies
        fish = a
        rabbit = b
        chicken = c
        
        days = 0
        
        # Simulate the days of the week
        for i in range(7):
            day_of_week = (start_day + i) % 7
            
            if day_of_week in [0, 3, 6]:  # Fish days
                if fish > 0:
                    fish -= 1
                    days += 1
                else:
                    break
            elif day_of_week in [1, 5]:  # Rabbit days
                if rabbit > 0:
                    rabbit -= 1
                    days += 1
                else:
                    break
            else:  # Chicken days
                if chicken > 0:
                    chicken -= 1
                    days += 1
                else:
                    break
        
        max_days = max(max_days, days)

    return max_days

# Input
a, b, c = map(int, input().split())
# Output
print(max_days(a, b, c))