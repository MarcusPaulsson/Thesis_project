def calculate_days_off(n):
    full_weeks = n // 7
    work_days = full_weeks * 5
    days_off = full_weeks * 2
    
    remaining_days = n % 7
    
    # Calculate minimum days off
    min_days_off = days_off
    # Calculate maximum days off
    max_days_off = days_off + min(remaining_days, 2)
    
    return min_days_off, max_days_off

n = int(input())
min_days_off, max_days_off = calculate_days_off(n)
print(min_days_off, max_days_off)