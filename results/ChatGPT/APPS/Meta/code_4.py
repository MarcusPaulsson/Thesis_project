def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, x):
    mm -= x
    if mm < 0:
        mm += 60
        hh -= 1
        if hh < 0:
            hh += 24
    return hh, mm

def minimum_snooze_presses(x, hh, mm):
    presses = 0
    while not is_lucky(hh, mm):
        hh, mm = time_before(hh, mm, x)
        presses += 1
    return presses

x = int(input())
hh, mm = map(int, input().split())
print(minimum_snooze_presses(x, hh, mm))