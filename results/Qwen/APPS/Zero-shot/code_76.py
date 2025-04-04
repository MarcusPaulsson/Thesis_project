def can_construct_symmetric_square(n, m, tiles):
    if m % 2 != 0:
        return "NO"
    for i in range(n):
        if tiles[i][0] != tiles[i][3] or tiles[i][1] != tiles[i][2]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tiles = [list(map(int, input().split())) for _ in range(2*n)]
    print(can_construct_symmetric_square(n, m, tiles))