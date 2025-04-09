def solve():
    n, m = map(int, input().split())

    if m % 2 != 0:
        print("NO")
        return

    tiles = []
    for _ in range(n):
        row1 = list(map(int, input().split()))
        row2 = list(map(int, input().split()))
        tiles.append((row1, row2))

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