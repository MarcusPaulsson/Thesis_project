n = int(input())

# Calculate minimum days off
min_days_off = 0 if n < 5 else (n // 7) * 2 + min(2, n % 7)

# Calculate maximum days off
max_days_off = min(2, n)

print(min_days_off, max_days_off)