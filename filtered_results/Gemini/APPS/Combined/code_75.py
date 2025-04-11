def solve():
    a, b, c = map(int, input().split())

    weekly_food = [1, 2, 3, 1, 3, 2, 1]
    weekly_fish = weekly_food.count(1)
    weekly_rabbit = weekly_food.count(2)
    weekly_chicken = weekly_food.count(3)

    weeks = min(a // weekly_fish, b // weekly_rabbit, c // weekly_chicken)
    a -= weeks * weekly_fish
    b -= weeks * weekly_rabbit
    c -= weeks * weekly_chicken
    days = weeks * 7

    max_days = 0
    for start_day in range(7):
        a_temp, b_temp, c_temp = a, b, c
        current_days = 0
        for i in range(7):
            food_type = weekly_food[(start_day + i) % 7]
            if food_type == 1:
                if a_temp > 0:
                    a_temp -= 1
                    current_days += 1
                else:
                    break
            elif food_type == 2:
                if b_temp > 0:
                    b_temp -= 1
                    current_days += 1
                else:
                    break
            else:
                if c_temp > 0:
                    c_temp -= 1
                    current_days += 1
                else:
                    break
        max_days = max(max_days, current_days)

    print(days + max_days)

solve()