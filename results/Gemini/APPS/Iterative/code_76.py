def solve():
    n, m = map(int, input().split())
    tiles = []
    for _ in range(n):
        tile1 = list(map(int, input().split()))
        tile2 = list(map(int, input().split()))
        tiles.append([tile1, tile2])

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