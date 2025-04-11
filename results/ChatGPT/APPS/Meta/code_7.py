def day_when_barn_empty(n, m):
    day = 0
    grains = n
    
    while grains > 0:
        day += 1
        grains += m  # grains brought to the barn
        if grains > n:
            grains = n  # barn is full, excess grains are ignored
        grains -= day  # sparrows eat grains
        
    return day

# Input reading
n, m = map(int, input().split())
print(day_when_barn_empty(n, m))