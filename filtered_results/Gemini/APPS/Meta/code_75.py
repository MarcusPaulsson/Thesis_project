def solve():
    a, b, c = map(int, input().split())
    
    days = [0] * 7
    days[0] = 0  # Monday
    days[1] = 1  # Tuesday
    days[2] = 2  # Wednesday
    days[3] = 0  # Thursday
    days[4] = 2  # Friday
    days[5] = 1  # Saturday
    days[6] = 0  # Sunday
    
    food = [a, b, c]
    
    def calculate_days(start_day):
        food_copy = food[:]
        count = 0
        day = start_day
        while True:
            food_type = days[day % 7]
            if food_copy[food_type] > 0:
                food_copy[food_type] -= 1
                count += 1
                day += 1
            else:
                break
        return count

    max_days = 0
    for start_day in range(7):
        max_days = max(max_days, calculate_days(start_day))
    
    print(max_days)

solve()