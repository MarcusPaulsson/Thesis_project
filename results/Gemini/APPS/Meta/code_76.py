def solve():
    n, m = map(int, input().split())
    tiles = []
    for _ in range(n):
        tiles.append([list(map(int, input().split())) for _ in range(2)])

    if m % 2 != 0:
        print("NO")
        return

    found = False
    for tile in tiles:
        if tile[0][1] == tile[1][0]:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()