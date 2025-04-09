def solve():
    n, m = map(int, input().split())
    
    grains = n
    day = 0
    
    while grains > 0:
        day += 1
        
        grains = min(n, grains + m)
        
        sparrows = day
        
        grains -= sparrows
        
        if grains < 0:
            grains = 0
            
    print(day)

solve()