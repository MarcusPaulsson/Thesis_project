n = int(input())

# Maximum days off: all days can be off if n is less than or equal to 2
max_days_off = min(n, 2)

# Minimum days off: calculate complete weeks and remaining days
full_weeks = n // 7
remaining_days = n % 7

# Each full week contributes 2 days off
min_days_off = full_weeks * 2

# Check the remaining days
if remaining_days >= 5:
    min_days_off += 2  # If there are 5 or more remaining days, there are 2 days off
elif remaining_days >= 2:
    min_days_off += 1  # If there are 2 to 4 remaining days, there is 1 day off
# If remaining_days is 0 or 1, no additional days off

print(min_days_off, max_days_off)