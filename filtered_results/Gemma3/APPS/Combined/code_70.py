def solve():
    start_time = list(map(int, input().split(':')))
    end_time = list(map(int, input().split(':')))
    
    start_hour = start_time[0]
    start_minute = start_time[1]
    end_hour = end_time[0]
    end_minute = end_time[1]
    
    total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)
    
    mid_minutes = total_minutes // 2
    
    mid_hour = start_hour + (mid_minutes // 60)
    mid_minute = start_minute + (mid_minutes % 60)
    
    if mid_minute >= 60:
        mid_hour += 1
        mid_minute -= 60
    
    mid_hour %= 24
    
    print(f"{mid_hour:02}:{mid_minute:02}")

solve()