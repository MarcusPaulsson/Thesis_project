def calculate_days_off(n):
    # Each week consists of 5 work days and 2 days off
    days_in_week = 7
    work_days = 5
    off_days = 2
    
    # Calculate total complete weeks in n days
    complete_weeks = n // days_in_week
    remaining_days = n % days_in_week
    
    # Maximum days off is determined by complete weeks and any remaining days
    max_days_off = complete_weeks * off_days + min(remaining_days, off_days)
    
    # Minimum days off occurs when we consider how the year starts
    min_days_off = 0 if n <= work_days else 0 if remaining_days <= work_days else off_days

    print(min_days_off, max_days_off)

# Read input
n = int(input().strip())
calculate_days_off(n)