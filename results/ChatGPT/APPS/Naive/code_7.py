def find_empty_day(n, m):
    day = 1
    grains = n

    while grains > 0:
        # Add grains to the barn
        grains += m
        # Ensure barn does not exceed capacity
        if grains > n:
            grains = n
        
        # Sparrows eat grains
        grains -= day
        day += 1

    return day - 1

# Read input
n, m = map(int, input().split())
# Output the day when the barn becomes empty
print(find_empty_day(n, m))