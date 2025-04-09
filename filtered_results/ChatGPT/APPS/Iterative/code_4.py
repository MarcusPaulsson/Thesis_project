def is_lucky(hh, mm):
    return '7' in f"{hh:02}{mm:02}"

def time_before(hh, mm, x, y):
    total_minutes = (hh * 60 + mm - y * x) % 1440  # wrap around after 24 hours
    return total_minutes // 60, total_minutes % 60

x = int(input().strip())
hh, mm = map(int, input().strip().split())

y = 0
while True:
    prev_hh, prev_mm = time_before(hh, mm, x, y)
    if is_lucky(prev_hh, prev_mm):
        print(y)
        break
    y += 1