def find_empty_day(n, m):
    day = 0
    total_eaten = 0
    
    while n > 0:
        day += 1
        n += m  # grains brought to the barn
        total_eaten += day  # total grains eaten by day 'day'
        
        n -= total_eaten  # subtract the grains eaten by sparrows
        if n < 0:
            return day  # barn becomes empty on this day
            
    return day

# Input reading
n, m = map(int, input().split())
print(find_empty_day(n, m))