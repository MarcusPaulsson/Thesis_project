def days_until_empty(n, m):
    day = 0
    total_grains = n
    
    while total_grains > 0:
        day += 1
        total_grains += m  # grains are brought to the barn
        if total_grains > n:
            total_grains = n  # barn is full
        
        total_grains -= day  # sparrows eat grains
        
    return day

# Input
n, m = map(int, input().split())
print(days_until_empty(n, m))