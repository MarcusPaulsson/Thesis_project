n = int(input())

# Calculate the number of complete weeks and remaining days
weeks = n // 7
remaining_days = n % 7

# Maximum days off is the total days off in complete weeks plus the days off in remaining days
max_days_off = weeks * 2 + min(remaining_days, 2)

# Minimum days off is determined by the number of complete weeks
# If there are remaining days, they can be either work days or days off
min_days_off = 0 if remaining_days < 5 else remaining_days - 5

print(min_days_off, max_days_off)