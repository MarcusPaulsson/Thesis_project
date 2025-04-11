def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, x, y):
    total_minutes = (hh * 60 + mm - y * x) % (24 * 60)
    return total_minutes // 60, total_minutes % 60

x = int(input().strip())
hh, mm = map(int, input().strip().split())

y = 0
while not is_lucky(*time_before(hh, mm, x, y)):
    y += 1

print(y)