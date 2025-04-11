def solve():
    n, m = map(int, input().split())

    day = 0
    grains = n
    
    while True:
        day += 1
        grains += m
        if grains > n:
            grains = n
        
        grains -= day
        
        if grains <= 0:
            print(day)
            return

solve()