def is_lucky_hour(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, x):
    total_minutes = hh * 60 + mm
    while total_minutes >= 0:
        yield divmod(total_minutes, 60)
        total_minutes -= x

def find_lucky_time(x, hh, mm):
    for presses, (h, m) in enumerate(time_before(hh, mm, x)):
        if is_lucky_hour(h, m):
            return presses
    return -1  # This should never happen as per problem guarantee

# Input reading
x = int(input().strip())
hh, mm = map(int, input().strip().split())

# Output the result
print(find_lucky_time(x, hh, mm))