def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def minutes_to_time(hh, mm, minutes):
    mm += minutes
    hh += mm // 60
    mm %= 60
    hh %= 24
    return hh, mm

x = int(input())
hh, mm = map(int, input().split())

y = 0
while not is_lucky(hh, mm):
    y += 1
    hh, mm = minutes_to_time(hh, mm, -x)

print(y)