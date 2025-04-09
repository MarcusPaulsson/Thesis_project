def solve():
    x = int(input())
    hh, mm = map(int, input().split())

    def is_lucky(h, m):
        return '7' in str(h) or '7' in str(m)

    def to_minutes(h, m):
        return h * 60 + m

    def to_time(minutes):
        h = (minutes // 60) % 24
        m = minutes % 60
        return h, m

    target_minutes = to_minutes(hh, mm)
    
    for presses in range(1000):
        alarm_minutes = (target_minutes - presses * x) % (24 * 60)
        alarm_h, alarm_m = to_time(alarm_minutes)
        if is_lucky(alarm_h, alarm_m):
            print(presses)
            return

solve()