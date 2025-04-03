def is_lucky(hh, mm):
    return '7' in f"{hh:02d}:{mm:02d}"

def time_minus_minutes(hh, mm, minutes):
    total_minutes = hh * 60 + mm - minutes
    if total_minutes < 0:
        total_minutes += 24 * 60  # Wrap around to the previous day
    return total_minutes // 60, total_minutes % 60

x = int(input().strip())
hh, mm = map(int, input().strip().split())

y = 0
while True:
    prev_hh, prev_mm = time_minus_minutes(hh, mm, x * y)
    if is_lucky(prev_hh, prev_mm):
        print(y)
        break
    y += 1