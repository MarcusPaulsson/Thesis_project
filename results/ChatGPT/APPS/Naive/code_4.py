def is_lucky_time(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, minutes):
    total_minutes = hh * 60 + mm - minutes
    if total_minutes < 0:
        total_minutes += 24 * 60
    return divmod(total_minutes, 60)

def minimum_snoozes(x, hh, mm):
    y = 0
    while True:
        prev_hh, prev_mm = time_before(hh, mm, x * y)
        if is_lucky_time(prev_hh, prev_mm):
            return y
        y += 1

# Input reading
x = int(input().strip())
hh, mm = map(int, input().strip().split())

# Output the result
print(minimum_snoozes(x, hh, mm))