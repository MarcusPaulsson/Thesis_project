def solve():
    a, b, c = map(int, input().split())
    
    days_in_week = [
        [0, 1, 0, 1, 0, 0, 1],  # Fish food days
        [0, 0, 1, 0, 0, 1, 0],  # Rabbit stew days
        [1, 0, 0, 0, 1, 0, 0]   # Chicken stake days
    ]
    
    def calculate_days(start_day):
        days = 0
        a_copy, b_copy, c_copy = a, b, c
        current_day = start_day
        
        while True:
            fish_needed = days_in_week[0][current_day]
            rabbit_needed = days_in_week[1][current_day]
            chicken_needed = days_in_week[2][current_day]
            
            if a_copy >= fish_needed and b_copy >= rabbit_needed and c_copy >= chicken_needed:
                a_copy -= fish_needed
                b_copy -= rabbit_needed
                c_copy -= chicken_needed
                days += 1
                current_day = (current_day + 1) % 7
            else:
                break
        
        return days
    
    max_days = 0
    for start_day in range(7):
        max_days = max(max_days, calculate_days(start_day))
    
    print(max_days)

solve()