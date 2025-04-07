def is_lucky(hour, minute):
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    time_str = hour_str + minute_str
    return '7' in time_str

def solve():
    x = int(input())
    hh, mm = map(int, input().split())
    
    total_minutes = hh * 60 + mm
    
    for y in range(1000):
        alarm_minutes = total_minutes - x * y
        
        alarm_hour = (alarm_minutes // 60) % 24
        alarm_minute = alarm_minutes % 60
        
        if alarm_hour < 0:
            alarm_hour += 24
        
        if is_lucky(alarm_hour, alarm_minute):
            print(y)
            return

solve()