def day_when_barn_empty(n, m):
    day = 0
    total_eaten = 0
    
    while n > 0:
        day += 1
        total_eaten += day  # Total sparrows that have come until today
        n += m  # Grains brought to the barn
        
        # If barn is full, it can only hold n grains
        if n > n:
            n = n  # Barn remains full
            
        n -= total_eaten  # Sparrows eat from the barn
        
    return day

# Input
n, m = map(int, input().split())
print(day_when_barn_empty(n, m))