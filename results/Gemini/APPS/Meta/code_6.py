def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        blows.append(list(map(int, input().split())))

    max_d = 0
    for d, h in blows:
        max_d = max(max_d, d)
    
    best_blow = None
    for d, h in blows:
        if d > h:
            if best_blow is None or (d - h) > (best_blow[0] - best_blow[1]):
                best_blow = (d, h)

    if max_d >= x:
        print(1)
        return
    
    if best_blow is None:
        print(-1)
        return
    
    d, h = best_blow
    diff = d - h
    
    remaining = x - max_d
    
    ans = (remaining + diff - 1) // diff + 1
    print(ans)
    

t = int(input())
for _ in range(t):
    solve()