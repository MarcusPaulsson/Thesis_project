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

    max_diff = float('-inf')
    for d, h in blows:
        max_diff = max(max_diff, d - h)

    if max_diff <= 0 and max_damage < x:
        print(-1)
        return

    if max_damage >= x:
        print(1)
        return

    remaining = x - max_damage
    blows_count = 1

    if max_diff <= 0:
      print(blows_count)
      return
    
    num_blows = (remaining + max_diff - 1) // max_diff
    blows_count += num_blows

    print(blows_count)


t = int(input())
for _ in range(t):
    solve()