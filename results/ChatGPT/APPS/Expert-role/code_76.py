def can_construct_symmetric_square(n, m, tiles):
    if m % 2 != 0:
        return "NO"
    
    top_left = set()
    top_right = set()
    bottom_left = set()
    bottom_right = set()
    
    for tile in tiles:
        tl, tr = tile[0]
        bl, br = tile[1]
        top_left.add(tl)
        top_right.add(tr)
        bottom_left.add(bl)
        bottom_right.add(br)
    
    # Check if we can form the symmetric pairs
    for tl in top_left:
        if tl in bottom_right:
            return "YES"
    for tr in top_right:
        if tr in bottom_left:
            return "YES"
    
    return "NO"

t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for _ in range(n):
        top = tuple(map(int, input().split()))
        bottom = tuple(map(int, input().split()))
        tiles.append((top, bottom))
    
    results.append(can_construct_symmetric_square(n, m, tiles))

print("\n".join(results))