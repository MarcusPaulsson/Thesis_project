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
    
    def calculate_days(start_day):
        days = 0
        a_temp, b_temp, c_temp = a, b, c
        current_day_index = days_of_week.index(start_day)
        
        while True:
            current_day = days_of_week[current_day_index % 7]
            food_type = food_schedule[current_day]
            
            if food_type == "fish":
                if a_temp > 0:
                    a_temp -= 1
                    days += 1
                else:
                    break
            elif food_type == "rabbit":
                if b_temp > 0:
                    b_temp -= 1
                    days += 1
                else:
                    break
            else:
                if c_temp > 0:
                    c_temp -= 1
                    days += 1
                else:
                    break
            
            current_day_index += 1
        
        return days

    max_days = 0
    for start_day in days_of_week:
        max_days = max(max_days, calculate_days(start_day))
    
    print(max_days)

solve()