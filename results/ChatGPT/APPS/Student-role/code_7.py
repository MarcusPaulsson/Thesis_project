def find_empty_day(n, m):
    day = 0
    total_grains = n
    
    while total_grains > 0:
        day += 1
        total_grains += m  # Grains brought to the barn
        if total_grains > n:
            total_grains = n  # Barn is full, excess grains are ignored
        total_grains -= day  # Sparrows eat grains
        
    return day

# Read input
n, m = map(int, input().split())
# Output the result
print(find_empty_day(n, m))