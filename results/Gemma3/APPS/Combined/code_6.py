from collections import deque

def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        d, h = map(int, input().split())
        blows.append((d, h))
    
    q = deque([(x, 0)])
    visited = {x}
    
    while q:
        cur_x, steps = q.popleft()
        
        if cur_x == 0:
            print(steps)
            return
        
        for d, h in blows:
            next_x = max(0, cur_x - min(d, cur_x))
            if next_x > 0:
                next_x += h
            
            if next_x not in visited and next_x <= 2 * x:
                visited.add(next_x)
                q.append((next_x, steps + 1))
    
    print(-1)

t = int(input())
for _ in range(t):
    solve()