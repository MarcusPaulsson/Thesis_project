def solve():
    n, m = map(int, input().split())
    
    day = 0
    grains = n
    
    while True:
        day += 1
        grains = min(n, grains + m)
        grains -= day
        
        if grains <= 0:
            print(day)
            return

solve()