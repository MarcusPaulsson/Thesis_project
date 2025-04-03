def max_days(a, b, c):
    # Food requirements based on day of the week
    days = [
        (1, 0, 0),  # Monday - fish food
        (1, 0, 0),  # Tuesday - fish food
        (0, 1, 0),  # Wednesday - rabbit stew
        (0, 1, 0),  # Thursday - rabbit stew
        (0, 0, 1),  # Friday - chicken stake
        (0, 0, 1),  # Saturday - chicken stake
        (1, 0, 0)   # Sunday - fish food
    ]

    max_days_count = 0

    for start_day in range(7):
        fish = a
        rabbit = b
        chicken = c
        days_count = 0
        
        for i in range(7):
            current_day = (start_day + i) % 7
            if days[current_day][0] > 0:  # Fish food required
                if fish > 0:
                    fish -= 1
                    days_count += 1
                else:
                    break
            elif days[current_day][1] > 0:  # Rabbit stew required
                if rabbit > 0:
                    rabbit -= 1
                    days_count += 1
                else:
                    break
            elif days[current_day][2] > 0:  # Chicken stake required
                if chicken > 0:
                    chicken -= 1
                    days_count += 1
                else:
                    break

        max_days_count = max(max_days_count, days_count)

    return max_days_count

# Input
a, b, c = map(int, input().split())
print(max_days(a, b, c))