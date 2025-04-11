def find_empty_day(n, m):
    day = 0
    total_eaten = 0
    
    while n > 0:
        day += 1
        total_eaten += day
        
        # Add grains to the barn
        n += m
        
        # If the barn is over capacity, it stays full
        if n > m:
            n = n  # Barn remains full
        else:
            n = n  # Barn is filled with the new grains
        
        # Sparrows eat grains
        n -= total_eaten
        
    return day

# Input reading
n, m = map(int, input().split())
print(find_empty_day(n, m))