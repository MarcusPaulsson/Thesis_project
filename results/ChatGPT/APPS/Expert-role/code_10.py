n = int(input())

# Maximum days off: all weekends can fit in the n days
max_days_off = (n // 7) * 2 + min(2, n % 7)

# Minimum days off: if there are fewer days than a full week
min_days_off = 0 if n < 5 else (n // 7) * 2 + (1 if n % 7 >= 5 else 0)

print(min_days_off, max_days_off)