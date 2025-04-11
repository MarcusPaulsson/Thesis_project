def calculate_days_off(n):
    complete_weeks = n // 7
    remaining_days = n % 7
    
    # Minimum days off: all complete weeks contribute 2 days off
    min_days_off = complete_weeks * 2
    
    # Maximum days off: can take days off from remaining days
    max_days_off = min_days_off + min(remaining_days, 2)
    
    return min_days_off, max_days_off

# Input
n = int(input().strip())
# Calculate and output the result
min_off, max_off = calculate_days_off(n)
print(min_off, max_off)