def find_empty_day(n, m):
    day = 0
    total_eaten = 0

    while n > 0:
        day += 1
        # Grains brought to the barn
        n += m
        
        # Sparrows eat grains
        total_eaten += day
        
        # If grains are eaten, reduce the barn's grain count
        n -= total_eaten
        
        # If barn is empty, break the loop
        if n <= 0:
            break
            
    return day

# Read input
n, m = map(int, input().split())
# Output the result
print(find_empty_day(n, m))