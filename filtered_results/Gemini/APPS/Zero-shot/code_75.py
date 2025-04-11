def solve():
    a, b, c = map(int, input().split())
    
    def calculate_days(start_day):
        days = 0
        a_temp, b_temp, c_temp = a, b, c
        
        while True:
            day = (start_day + days) % 7
            
            if day in [0, 3, 6]:  # Monday, Thursday, Sunday
                if a_temp > 0:
                    a_temp -= 1
                else:
                    break
            elif day in [1, 5]:  # Tuesday, Saturday
                if b_temp > 0:
                    b_temp -= 1
                else:
                    break
            else:  # Wednesday, Friday
                if c_temp > 0:
                    c_temp -= 1
                else:
                    break
            
            days += 1
        
        return days
    
    max_days = 0
    for start_day in range(7):
        max_days = max(max_days, calculate_days(start_day))
    
    print(max_days)

solve()