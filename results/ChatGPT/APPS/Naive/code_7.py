def days_until_empty(n, m):
    day = 0
    total_sparrows = 0
    current_grains = n

    while current_grains > 0:
        day += 1
        total_sparrows += day
        
        # Add grains to the barn
        current_grains += m
        
        # If the barn exceeds its capacity, it remains full
        if current_grains > n:
            current_grains = n
        
        # Sparrows eat grains
        current_grains -= total_sparrows
        
    return day

# Input reading
n, m = map(int, input().split())
print(days_until_empty(n, m))