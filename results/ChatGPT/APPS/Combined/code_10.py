def calculate_days_off(n):
    # Constants for work days and days off in a week
    WORK_DAYS = 5
    DAYS_OFF = 2
    WEEK_LENGTH = WORK_DAYS + DAYS_OFF
    
    # Calculate total complete weeks and remaining days
    total_weeks = n // WEEK_LENGTH
    remaining_days = n % WEEK_LENGTH
    
    # Minimum days off is determined by complete weeks
    min_days_off = total_weeks * DAYS_OFF
    
    # Maximum days off can include remaining days if they are days off
    max_days_off = min_days_off + min(remaining_days, DAYS_OFF)
    
    return min_days_off, max_days_off

# Input reading
n = int(input().strip())
min_days, max_days = calculate_days_off(n)
print(min_days, max_days)