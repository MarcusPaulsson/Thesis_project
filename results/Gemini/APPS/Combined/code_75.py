def solve():
    a, b, c = map(int, input().split())
    
    week_food = [3, 2, 2]
    food_needed = [a, b, c]
    
    full_weeks = min(food_needed[i] // week_food[i] for i in range(3))
    
    a -= full_weeks * week_food[0]
    b -= full_weeks * week_food[1]
    c -= full_weeks * week_food[2]
    
    days = full_weeks * 7
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    food_types = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 0,
        "Friday": 2,
        "Saturday": 1,
        "Sunday": 0
    }
    
    max_remaining_days = 0
    for start_day in range(7):
        remaining_a = a
        remaining_b = b
        remaining_c = c
        
        remaining_days = 0
        current_day = start_day
        
        while True:
            food_type = food_types[days_of_week[current_day % 7]]
            
            if food_type == 0:
                if remaining_a > 0:
                    remaining_a -= 1
                    remaining_days += 1
                else:
                    break
            elif food_type == 1:
                if remaining_b > 0:
                    remaining_b -= 1
                    remaining_days += 1
                else:
                    break
            else:
                if remaining_c > 0:
                    remaining_c -= 1
                    remaining_days += 1
                else:
                    break
            
            current_day += 1
        
        max_remaining_days = max(max_remaining_days, remaining_days)
    
    print(days + max_remaining_days)

solve()