def solve():
    x = int(input())
    hh, mm = map(int, input().split())
    
    wake_up_minutes = hh * 60 + mm
    
    for y in range(1000):
        alarm_minutes = (wake_up_minutes - x * y) % (24 * 60)
        
        alarm_hh = alarm_minutes // 60
        alarm_mm = alarm_minutes % 60
        
        alarm_time_str = "{:02d}:{:02d}".format(alarm_hh, alarm_mm)
        
        if '7' in alarm_time_str:
            print(y)
            return
            
solve()