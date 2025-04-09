n = int(input())

# Calculate the number of weeks and the remaining days
weeks = n // 7
remaining_days = n % 7

# Minimum days off
min_days_off = weeks * 2
if remaining_days > 5:
    min_days_off += 2
elif remaining_days > 0:
    min_days_off += 0

# Maximum days off
max_days_off = weeks * 2 + min(remaining_days, 2)

print(min_days_off, max_days_off)