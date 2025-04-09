def is_lucky(hh, mm):
    return '7' in f"{hh:02d}:{mm:02d}"

def time_before(hh, mm, x, y):
    total_minutes = hh * 60 + mm - x * y
    total_minutes %= 1440  # wrap around after 24 hours
    return total_minutes // 60, total_minutes % 60

x = int(input())
hh, mm = map(int, input().split())

y = 0
while True:
    prev_hh, prev_mm = time_before(hh, mm, x, y)
    if is_lucky(prev_hh, prev_mm):
        print(y)
        break
    y += 1