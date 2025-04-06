def solve():
    a, b, c = map(int, input().split())
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    food_schedule = {
        "Monday": "fish",
        "Tuesday": "rabbit",
        "Wednesday": "chicken",
        "Thursday": "fish",
        "Friday": "chicken",
        "Saturday": "rabbit",
        "Sunday": "fish"
    }
    
    max_days = 0
    
    for start_day_index in range(7):
        current_a = a
        current_b = b
        current_c = c
        
        days = 0
        
        current_day_index = start_day_index
        
        while True:
            day_name = days_of_week[current_day_index % 7]
            food_type = food_schedule[day_name]
            
            if food_type == "fish":
                if current_a > 0:
                    current_a -= 1
                    days += 1
                else:
                    break
            elif food_type == "rabbit":
                if current_b > 0:
                    current_b -= 1
                    days += 1
                else:
                    break
            else:
                if current_c > 0:
                    current_c -= 1
                    days += 1
                else:
                    break
            
            current_day_index += 1
            
        max_days = max(max_days, days)
    
    print(max_days)
    
solve()