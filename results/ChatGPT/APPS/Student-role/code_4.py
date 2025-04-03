def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def minutes_before(hh, mm, x, y):
    total_minutes = hh * 60 + mm - y * x
    if total_minutes < 0:
        total_minutes += 24 * 60  # wrap around to the previous day
    return total_minutes // 60, total_minutes % 60

x = int(input())
hh, mm = map(int, input().split())

y = 0
while not is_lucky(*minutes_before(hh, mm, x, y)):
    y += 1

print(y)