def day_when_barn_empty(n, m):
    day = 0
    grains = n
    
    while grains > 0:
        day += 1
        grains = min(grains + m, n)  # Add grains to the barn, respecting capacity
        grains -= day  # Sparrows eat grains
        
    return day

# Read input
n, m = map(int, input().split())
# Output the result
print(day_when_barn_empty(n, m))