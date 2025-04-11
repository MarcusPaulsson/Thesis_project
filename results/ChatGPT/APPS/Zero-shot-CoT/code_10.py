n = int(input())

# Calculate the number of complete weeks and remaining days
weeks = n // 7
remaining_days = n % 7

# Minimum days off is when all remaining days are work days
min_days_off = weeks * 2

# Maximum days off is when all remaining days are days off
max_days_off = min(remaining_days, 2) + weeks * 2

print(min_days_off, max_days_off)