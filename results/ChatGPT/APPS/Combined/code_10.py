def calculate_days_off(n):
    # Maximum possible days off
    max_days_off = min(n, 2)

    # Minimum possible days off calculation
    full_weeks = n // 7
    remaining_days = n % 7
    
    min_days_off = full_weeks * 2
    if remaining_days >= 5:
        min_days_off += 2

    return min_days_off, max_days_off

# Read input
n = int(input().strip())
# Calculate and print the result
result = calculate_days_off(n)
print(result[0], result[1])