def find_empty_day(n, m):
    day = 0
    grains = n

    while grains > 0:
        day += 1
        grains = min(grains + m, n)  # Add grains brought to the barn, respecting capacity
        grains -= day  # Sparrows eat grains equal to the day number
        
    return day

# Input reading
n, m = map(int, input().split())
print(find_empty_day(n, m))