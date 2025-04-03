n = int(input())

# Calculate minimum days off
if n < 5:
    min_days_off = 0
else:
    min_days_off = n // 7 * 2 + max(0, n % 7 - 5)

# Calculate maximum days off
max_days_off = min(n, 2 + (n // 7) * 2)

print(min_days_off, max_days_off)