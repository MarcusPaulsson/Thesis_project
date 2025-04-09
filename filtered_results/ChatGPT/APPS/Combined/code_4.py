def is_lucky_time(hh, mm):
    """Check if the given time contains the digit '7'."""
    return '7' in f"{hh:02d}{mm:02d}"

def time_before(hh, mm, minutes):
    """Calculate the time that is a certain number of minutes before the given time."""
    total_minutes = hh * 60 + mm - minutes
    if total_minutes < 0:
        total_minutes += 24 * 60  # Wrap around to the previous day
    return divmod(total_minutes, 60)

def min_snooze_presses(x, hh, mm):
    """Determine the minimum number of snooze presses needed to reach a lucky time."""
    presses = 0
    while not is_lucky_time(hh, mm):
        presses += 1
        hh, mm = time_before(hh, mm, x)
    return presses

# Input reading
x = int(input().strip())
hh, mm = map(int, input().strip().split())

# Output the result
print(min_snooze_presses(x, hh, mm))