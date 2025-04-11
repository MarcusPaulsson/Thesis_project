def is_lucky_time(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, minutes):
    total_minutes = (hh * 60 + mm - minutes) % (24 * 60)
    return divmod(total_minutes, 60)

def minimum_snooze_presses(x, hh, mm):
    presses = 0
    while not is_lucky_time(hh, mm):
        presses += 1
        hh, mm = time_before(hh, mm, x)
    return presses

# Input reading
x = int(input().strip())
hh, mm = map(int, input().strip().split())

# Output the result
print(minimum_snooze_presses(x, hh, mm))