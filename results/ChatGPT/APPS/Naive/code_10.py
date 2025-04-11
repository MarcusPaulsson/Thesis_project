def calculate_days_off(n):
    work_days_per_week = 5
    days_off_per_week = 2
    total_days_in_week = work_days_per_week + days_off_per_week

    full_weeks = n // total_days_in_week
    remaining_days = n % total_days_in_week

    max_days_off = full_weeks * days_off_per_week + min(remaining_days, days_off_per_week)
    min_days_off = full_weeks * days_off_per_week + (1 if remaining_days > work_days_per_week else 0)

    return min_days_off, max_days_off

n = int(input())
min_days_off, max_days_off = calculate_days_off(n)
print(min_days_off, max_days_off)