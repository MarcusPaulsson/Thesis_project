def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def previous_time(hh, mm, x):
    mm -= x
    if mm < 0:
        mm += 60
        hh -= 1
        if hh < 0:
            hh += 24
    return hh, mm

x = int(input())
hh, mm = map(int, input().split())

y = 0
while not is_lucky(hh, mm):
    y += 1
    hh, mm = previous_time(hh, mm, x)

print(y)