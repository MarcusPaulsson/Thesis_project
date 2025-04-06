def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        blows.append(list(map(int, input().split())))

    max_damage = 0
    for d, h in blows:
        max_damage = max(max_damage, d)

    max_diff = 0
    for d, h in blows:
        max_diff = max(max_diff, d - h)

    if max_damage >= x:
        print(1)
        return

    if max_diff <= 0:
        if max_damage <= 0:
            print(-1)
        else:
            print(-1)
        return
    
    remaining = x - max_damage
    
    ans = 1 + (remaining + max_diff - 1) // max_diff
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()