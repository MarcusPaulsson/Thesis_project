def days_until_empty(n, m):
    day = 0
    total_eaten = 0
    
    while n > 0:
        day += 1
        total_eaten += day
        
        # Add grains to the barn
        n += m
        
        # If the barn is over capacity, it remains full
        if n > m:
            n = m
        
        # Sparrows eat grains
        n -= total_eaten
        
        # Ensure n does not go below zero
        n = max(n, 0)
        
    return day

# Read input
n, m = map(int, input().split())
print(days_until_empty(n, m))