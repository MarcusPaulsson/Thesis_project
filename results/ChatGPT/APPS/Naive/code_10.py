def calculate_days_off(n):
    # Maximum days off are limited by the number of weekends that can fit in n days
    full_weeks = n // 7
    max_days_off = full_weeks * 2 + min(2, n % 7)
    
    # Minimum days off occur when we utilize the work days as much as possible
    if n < 5:
        min_days_off = n % 7 if n % 7 <= 2 else 0
    else:
        min_days_off = max_days_off
    
    return min_days_off, max_days_off

n = int(input())
min_off, max_off = calculate_days_off(n)
print(min_off, max_off)