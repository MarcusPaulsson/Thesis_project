def day_when_barn_empty(n, m):
    current_grains = n
    day = 1
    
    while current_grains > 0:
        # Grains are brought to the barn
        current_grains += m
        # Check if the barn overflows
        if current_grains > n:
            current_grains = n
        
        # Sparrows eat grains
        current_grains -= day
        
        # Move to the next day
        day += 1
    
    return day - 1  # Subtract 1 to get the last day it was not empty

# Read input
n, m = map(int, input().split())
# Calculate and print the result
print(day_when_barn_empty(n, m))