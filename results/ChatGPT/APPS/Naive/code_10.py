def calculate_days_off(n):
    # Calculate maximum days off
    max_days_off = min(n, (n // 7) * 2 + min(2, n % 7))
    
    # Calculate minimum days off
    if n < 5:
        min_days_off = n  # All days can be days off if less than 5
    else:
        min_days_off = (n // 7) * 2  # Full weeks contribute 2 days off
    
    print(min_days_off, max_days_off)

# Read input
n = int(input().strip())
calculate_days_off(n)