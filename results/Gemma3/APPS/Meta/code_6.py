def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        d, h = map(int, input().split())
        blows.append((d, h))
    
    q = [(x, 0)]
    visited = {x}
    
    while q:
        cur_x, steps = q.pop(0)
        
        if cur_x == 0:
            print(steps)
            return
        
        for d, h in blows:
            next_x = cur_x - min(d, cur_x)
            if next_x >= 0:
                next_x += h
            else:
                next_x = 0
            
            if next_x not in visited and next_x <= 10**9:
                q.append((next_x, steps + 1))
                visited.add(next_x)
    
    print(-1)

t = int(input())
for _ in range(t):
    solve()