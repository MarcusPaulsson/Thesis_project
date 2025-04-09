def is_lucky(hh, mm):
    return '7' in f"{hh:02d}:{mm:02d}"

def minutes_to_hh_mm(hh, mm, minutes):
    total_minutes = hh * 60 + mm - minutes
    if total_minutes < 0:
        total_minutes += 24 * 60  # wrap around to previous day
    return divmod(total_minutes, 60)

x = int(input())
hh, mm = map(int, input().split())

y = 0
while True:
    prev_hh, prev_mm = minutes_to_hh_mm(hh, mm, x * y)
    if is_lucky(prev_hh, prev_mm):
        print(y)
        break
    y += 1