def find_empty_day(n, m):
    day = 0
    total_eaten = 0
    
    while True:
        day += 1
        total_eaten += day
        
        # Calculate the amount of grain in the barn at the start of the day
        n = min(n + m, n)  # Barn cannot exceed its capacity
        
        # Subtract the eaten grains
        n -= total_eaten
        
        if n <= 0:
            return day

# Read input
n, m = map(int, input().split())
print(find_empty_day(n, m))