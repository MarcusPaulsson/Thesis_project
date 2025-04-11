def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def minutes_to_time(hh, mm, minutes):
    total_minutes = hh * 60 + mm - minutes
    total_minutes %= 1440  # Wrap around after 24 hours
    return divmod(total_minutes, 60)

def minimum_snoozes(x, hh, mm):
    y = 0
    while True:
        alarm_hh, alarm_mm = minutes_to_time(hh, mm, x * y)
        if is_lucky(alarm_hh, alarm_mm):
            return y
        y += 1

x = int(input())
hh, mm = map(int, input().split())
print(minimum_snoozes(x, hh, mm))