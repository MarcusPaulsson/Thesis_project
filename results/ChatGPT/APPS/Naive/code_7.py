def day_when_barn_empty(n, m):
    day = 1
    total_grains = n
    while total_grains > 0:
        # Add grains to the barn
        total_grains += m
        # If it exceeds the capacity, it remains full
        if total_grains > n:
            total_grains = n
        
        # Sparrows eat grains
        total_grains -= day
        
        # Move to the next day
        day += 1
    
    return day - 1  # Return the last day before it became empty

# Input reading
n, m = map(int, input().split())
# Output the result
print(day_when_barn_empty(n, m))