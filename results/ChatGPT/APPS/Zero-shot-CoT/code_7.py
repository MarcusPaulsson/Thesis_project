def day_when_barn_empty(n, m):
    day = 1
    grains = n

    while grains > 0:
        # Add grains to the barn
        grains += m
        if grains > n:
            grains = n  # Barn can't exceed its capacity
            
        # Sparrows eat grains
        grains -= day
        day += 1

    return day - 1

# Input
n, m = map(int, input().split())
print(day_when_barn_empty(n, m))