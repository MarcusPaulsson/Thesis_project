def contains_lucky_digit(hh, mm):
    """Check if the given hour and minute contain the lucky digit '7'."""
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, minutes):
    """Calculate the time that is 'minutes' before the given hh:mm."""
    total_minutes = hh * 60 + mm - minutes
    total_minutes = total_minutes % (24 * 60)  # wrap around for 24 hours
    return divmod(total_minutes, 60)  # returns (hh, mm)

def minimum_snooze_presses(x, hh, mm):
    """Calculate the minimum number of snooze presses required for a lucky time."""
    presses = 0
    while not contains_lucky_digit(hh, mm):
        hh, mm = time_before(hh, mm, x)
        presses += 1
    return presses

# Input
x = int(input())
hh, mm = map(int, input().split())

# Output
print(minimum_snooze_presses(x, hh, mm))