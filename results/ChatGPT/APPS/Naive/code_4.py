def is_lucky_time(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_minus_x_minutes(hh, mm, x):
    mm -= x
    if mm < 0:
        mm += 60
        hh -= 1
    if hh < 0:
        hh += 24
    return hh, mm

def find_lucky_snooze_count(x, hh, mm):
    count = 0
    while not is_lucky_time(hh, mm):
        count += 1
        hh, mm = time_minus_x_minutes(hh, mm, x)
    return count

# Input reading
x = int(input().strip())
hh, mm = map(int, input().strip().split())

# Calculate and print the result
print(find_lucky_snooze_count(x, hh, mm))