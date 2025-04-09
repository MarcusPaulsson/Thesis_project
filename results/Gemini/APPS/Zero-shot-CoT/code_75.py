def solve():
    a, b, c = map(int, input().split())
    
    days_in_week = [
        [0],  # Monday: 0 for fish
        [1],  # Tuesday: 1 for rabbit
        [2],  # Wednesday: 2 for chicken
        [0],  # Thursday: 0 for fish
        [2],  # Friday: 2 for chicken
        [1],  # Saturday: 1 for rabbit
        [0]   # Sunday: 0 for fish
    ]
    
    def calculate_days(start_day):
        days = 0
        a_copy, b_copy, c_copy = a, b, c
        current_day = start_day
        
        while True:
            food_type = days_in_week[current_day][0]
            
            if food_type == 0:
                if a_copy > 0:
                    a_copy -= 1
                else:
                    break
            elif food_type == 1:
                if b_copy > 0:
                    b_copy -= 1
                else:
                    break
            else:
                if c_copy > 0:
                    c_copy -= 1
                else:
                    break
            
            days += 1
            current_day = (current_day + 1) % 7
        
        return days
    
    max_days = 0
    for start_day in range(7):
        max_days = max(max_days, calculate_days(start_day))
    
    print(max_days)

solve()