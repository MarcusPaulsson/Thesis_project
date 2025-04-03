n = int(input())

# Calculate minimum days off
min_days_off = (n // 7) * 2
# Calculate maximum days off
max_days_off = min(n, (n // 7) * 2 + (2 if n % 7 > 5 else n % 7))

print(min_days_off, max_days_off)