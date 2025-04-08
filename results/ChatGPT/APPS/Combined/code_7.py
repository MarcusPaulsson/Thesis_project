def day_when_barn_empty(n, m):
    grains = n
    day = 0
    
    while grains > 0:
        day += 1
        grains = min(n, grains + m)  # Add grains and ensure it doesn't exceed capacity
        grains -= day  # Sparrows eat grains
        
    return day

# Read input
n, m = map(int, input().split())
print(day_when_barn_empty(n, m))