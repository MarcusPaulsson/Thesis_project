def days_until_empty(n, m):
    day = 0
    total_eaten = 0

    while n > 0:
        day += 1
        n += m  # Add grains brought that day
        if n > m:  # Ensure barn does not exceed capacity
            n = n  # No need to change n, it remains up to capacity
        
        total_eaten += day  # Total grains eaten by sparrows

        n -= total_eaten  # Subtract the total grains eaten by sparrows

    return day

# Read input
n, m = map(int, input().split())
print(days_until_empty(n, m))