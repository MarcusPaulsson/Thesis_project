n = int(input())

# Calculate the maximum days off
max_days_off = (n // 7) * 2 + min(2, n % 7)

# Calculate the minimum days off
# If there are less than 5 work days, all can be days off
min_days_off = 0 if n >= 5 else n

print(min_days_off, max_days_off)