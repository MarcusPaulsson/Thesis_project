def is_lucky_time(hour, minute):
    """Checks if a time is lucky (contains the digit '7')."""
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    time_str = hour_str + minute_str
    return '7' in time_str

def solve():
    """Solves the problem of finding the minimum snooze button presses."""
    x = int(input())
    hh, mm = map(int, input().split())

    total_minutes = hh * 60 + mm
    
    for y in range(1000):  # Iterate through possible snooze counts
        alarm_minutes = total_minutes - x * y
        
        alarm_hour = (alarm_minutes // 60) % 24
        alarm_minute = alarm_minutes % 60
        
        if is_lucky_time(alarm_hour, alarm_minute):
            print(y)
            return

solve()