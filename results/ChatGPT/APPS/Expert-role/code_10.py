n = int(input().strip())

work_days = n // 7 * 5
days_off = n // 7 * 2

remaining_days = n % 7

if remaining_days > 5:
    days_off += 2
elif remaining_days > 0:
    days_off += remaining_days

min_days_off = days_off
max_days_off = days_off + (2 if remaining_days > 0 else 0)

print(min_days_off, max_days_off)