n = int(input())

# Calculate maximum days off
max_days_off = (n // 7) * 2 + min(2, n % 7)

# Calculate minimum days off
if n >= 5:
    min_days_off = 0
else:
    min_days_off = max(0, n - 5)

print(min_days_off, max_days_off)