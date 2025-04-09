def solve():
    n = int(input())
    reachable = set()
    reachable.add(n)
    
    current = n
    while True:
        current += 1
        while current % 10 == 0:
            current //= 10
        
        if current in reachable:
            break
        else:
            reachable.add(current)
            
    print(len(reachable))

solve()