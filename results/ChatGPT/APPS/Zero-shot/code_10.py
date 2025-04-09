n = int(input())

# Calculate the maximum days off
max_days_off = (n // 7) * 2 + min(2, n % 7)

# Calculate the minimum days off
if n < 5:
    min_days_off = 0
else:
    min_days_off = (n // 7) * 2

print(min_days_off, max_days_off)