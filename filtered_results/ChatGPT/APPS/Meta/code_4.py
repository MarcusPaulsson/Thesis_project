def is_lucky_time(hh, mm):
    return '7' in f'{hh:02d}{mm:02d}'

def time_before(hh, mm, minutes):
    mm -= minutes
    if mm < 0:
        mm += 60
        hh -= 1
        if hh < 0:
            hh += 24
    return hh, mm

x = int(input().strip())
hh, mm = map(int, input().strip().split())

presses = 0
while not is_lucky_time(hh, mm):
    presses += 1
    hh, mm = time_before(hh, mm, x)

print(presses)