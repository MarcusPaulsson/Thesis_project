def find_empty_day(n, m):
    grains = n
    day = 1
    
    while True:
        # Add grains to the barn
        grains += m
        if grains > n:
            grains = n
        
        # Sparrows eat grains
        grains -= day
        if grains <= 0:
            return day
        
        day += 1

# Input
n, m = map(int, input().split())
print(find_empty_day(n, m))