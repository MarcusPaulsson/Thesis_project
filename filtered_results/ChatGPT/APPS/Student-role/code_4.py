def is_lucky(hh, mm):
    return '7' in f"{hh:02d}{mm:02d}"

def time_to_minutes(hh, mm):
    return hh * 60 + mm

def minutes_to_time(total_minutes):
    hh = (total_minutes // 60) % 24
    mm = total_minutes % 60
    return hh, mm

# Input
x = int(input())
hh, mm = map(int, input().split())

# Calculate the target time in minutes
target_time = time_to_minutes(hh, mm)

# Initialize the snooze count
snooze_count = 0

# Check for lucky times
while True:
    current_time = target_time - snooze_count * x
    if current_time < 0:
        current_time += 24 * 60  # Wrap around to the previous day
    current_hh, current_mm = minutes_to_time(current_time)
    
    if is_lucky(current_hh, current_mm):
        print(snooze_count)
        break
    
    snooze_count += 1