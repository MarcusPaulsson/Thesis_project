def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def minutes_before(hh, mm, x, y):
    total_minutes = hh * 60 + mm - x * y
    if total_minutes < 0:
        total_minutes += 24 * 60
    return total_minutes // 60, total_minutes % 60

x = int(input().strip())
hh, mm = map(int, input().strip().split())

y = 0
while True:
    prev_hh, prev_mm = minutes_before(hh, mm, x, y)
    if is_lucky(prev_hh, prev_mm):
        print(y)
        break
    y += 1