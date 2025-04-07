def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, minutes):
    total_minutes = (hh * 60 + mm - minutes) % (24 * 60)
    return divmod(total_minutes, 60)

def min_snoozes(x, hh, mm):
    y = 0
    while not is_lucky(*time_before(hh, mm, x * y)):
        y += 1
    return y

x = int(input().strip())
hh, mm = map(int, input().strip().split())

print(min_snoozes(x, hh, mm))