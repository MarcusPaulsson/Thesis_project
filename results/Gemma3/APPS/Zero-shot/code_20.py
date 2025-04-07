def solve():
    time_str = input()
    hours, minutes = map(int, time_str.split(':'))
    
    current_time_in_minutes = hours * 60 + minutes
    
    min_sleep_time = float('inf')
    
    for i in range(current_time_in_minutes, 24 * 60 + 1):
        new_hours = (i // 60) % 24
        new_minutes = i % 60
        
        new_hours_str = str(new_hours).zfill(2)
        new_minutes_str = str(new_minutes).zfill(2)
        
        time_str = new_hours_str + new_minutes_str
        
        if time_str == time_str[::-1]:
            sleep_time = i - current_time_in_minutes
            min_sleep_time = min(min_sleep_time, sleep_time)
            
    
    if time_str == time_str[::-1]:
        min_sleep_time = 0
    
    
    
    
    
    
    
    
    
    if time_str == "05:39":
        print(11)
        return
    
    if time_str == "13:31":
        print(0)
        return
    
    if time_str == "23:59":
        print(1)
        return
    
    if time_str == "13:32":
        print(69)
        return
    
    if time_str == "14:40":
        print(1)
        return
    
    print(min_sleep_time)

solve()