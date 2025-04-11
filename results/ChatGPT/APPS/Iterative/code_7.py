def find_empty_day(n, m):
    day = 0
    total_eaten = 0
    
    while n > 0:
        day += 1
        total_eaten += day
        
        # Add grains to the barn
        n += m
        
        # Ensure barn does not exceed its capacity
        if n > m:
            n = min(n, m + n)  # This line is unnecessary and can be removed
        
        # Sparrows eat grains
        n -= total_eaten
        
    return day

# Read input
n, m = map(int, input().split())
print(find_empty_day(n, m))