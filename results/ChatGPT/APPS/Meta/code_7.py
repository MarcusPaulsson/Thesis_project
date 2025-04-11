def find_empty_day(n, m):
    day = 0
    total_eaten = 0
    
    while n > 0:
        day += 1
        n = min(n + m, n)  # Add grains to the barn, but it can't exceed its capacity
        total_eaten += day  # Total grains eaten by sparrows up to this day
        n -= total_eaten  # Update the number of grains in the barn after sparrows eat
        
    return day

# Read input
n, m = map(int, input().split())
print(find_empty_day(n, m))