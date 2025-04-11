def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        blows.append(list(map(int, input().split())))

    max_damage = 0
    for d, h in blows:
        max_damage = max(max_damage, d)

    ans = float('inf')

    for d, h in blows:
        if d >= x:
            ans = min(ans, 1)

    if ans == 1:
        print(1)
        return

    
    max_diff = 0
    for d, h in blows:
        max_diff = max(max_diff, d - h)

    if max_diff <= 0 and max_damage < x:
        print(-1)
        return

    if max_diff <= 0:
        print(-1)
        return

    
    remaining = x - max_damage
    
    if remaining <= 0:
        print(2)
        return

    
    blows_needed = (remaining + max_diff - 1) // max_diff
    
    print(blows_needed + 1)
    

t = int(input())
for _ in range(t):
    solve()