def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        blows.append(list(map(int, input().split())))

    min_blows = float('inf')

    for i in range(n):
        if blows[i][0] >= x:
            min_blows = 1
            break
    
    if min_blows == 1:
        print(1)
        return

    max_damage = 0
    for d, h in blows:
        max_damage = max(max_damage, d)

    max_diff = 0
    for d, h in blows:
        max_diff = max(max_diff, d - h)

    if max_diff <= 0:
        if max_damage >= x:
            print(1)
        else:
            print(-1)
        return

    
    blows_needed = (x - max_damage + max_diff - 1) // max_diff + 1

    print(blows_needed)


t = int(input())
for _ in range(t):
    solve()