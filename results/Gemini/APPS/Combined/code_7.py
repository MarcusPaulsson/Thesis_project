def solve():
    n, m = map(int, input().split())

    capacity = n
    day = 0
    
    while True:
        day += 1
        capacity = min(n, capacity + m)
        capacity -= day
        
        if capacity <= 0:
            print(day)
            return

solve()