def calculate_days_off(n):
    # Constants
    WORK_DAYS = 5
    OFF_DAYS = 2
    WEEK_LENGTH = WORK_DAYS + OFF_DAYS
    
    # Complete weeks and remaining days calculation
    complete_weeks = n // WEEK_LENGTH
    remaining_days = n % WEEK_LENGTH
    
    # Minimum days off based on complete weeks
    min_days_off = complete_weeks * OFF_DAYS
    
    # Maximum days off includes remaining days if they fall within off days
    max_days_off = min_days_off + min(remaining_days, OFF_DAYS)
    
    return min_days_off, max_days_off

# Read input
n = int(input().strip())

# Calculate and print the result
min_off, max_off = calculate_days_off(n)
print(min_off, max_off)