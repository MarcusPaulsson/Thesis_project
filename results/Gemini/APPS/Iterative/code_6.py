def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        blows.append(list(map(int, input().split())))

    max_d = 0
    for d, h in blows:
        max_d = max(max_d, d)

    if max_d >= x:
        print(1)
        return

    max_diff = 0
    for d, h in blows:
        max_diff = max(max_diff, d - h)
    
    if max_diff <= 0:
        print(-1)
        return

    remaining = x - max_d
    ans = 1
    ans += (remaining + max_diff - 1) // max_diff
    print(ans)


t = int(input())
for _ in range(t):
    solve()