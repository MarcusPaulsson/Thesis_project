def find_empty_day(n, m):
    day = 0
    total_sparrows = 0
    grains = n

    while grains > 0:
        day += 1
        total_sparrows += day
        
        # Add grains to the barn
        grains = min(grains + m, n)
        
        # Sparrows eat grains
        grains -= total_sparrows
        
    return day

# Input reading
n, m = map(int, input().split())
print(find_empty_day(n, m))