def max_days(a, b, c):
    # Full week consumption
    week_consumption = [2, 1, 1]  # fish, rabbit, chicken for Mon, Tue, Wed, Thu, Fri, Sat, Sun
    week_days = 7

    # Calculate full weeks we can sustain
    full_weeks = min(a // week_consumption[0], b // week_consumption[1], c // week_consumption[2])
    days = full_weeks * week_days

    # Remaining food after full weeks
    a -= full_weeks * week_consumption[0]
    b -= full_weeks * week_consumption[1]
    c -= full_weeks * week_consumption[2]

    # Check starting from each day of the week to maximize days
    max_additional_days = 0
    for start_day in range(week_days):
        remaining_a, remaining_b, remaining_c = a, b, c
        additional_days = 0
        for day in range(week_days):
            current_day = (start_day + day) % week_days
            if current_day in [0, 3, 6]:  # Fish food days
                if remaining_a > 0:
                    remaining_a -= 1
                    additional_days += 1
                else:
                    break
            elif current_day in [1, 5]:  # Rabbit stew days
                if remaining_b > 0:
                    remaining_b -= 1
                    additional_days += 1
                else:
                    break
            else:  # Chicken stake days
                if remaining_c > 0:
                    remaining_c -= 1
                    additional_days += 1
                else:
                    break

        max_additional_days = max(max_additional_days, additional_days)

    return days + max_additional_days

# Read input
a, b, c = map(int, input().split())
print(max_days(a, b, c))