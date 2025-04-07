def can_construct_square(n, m, tiles):
    if m % 2 != 0:
        return "NO"
    
    # To construct a symmetric matrix, we need matching tiles
    tile_pairs = set()

    for tile in tiles:
        top_left, top_right = tile[0]
        bottom_left, bottom_right = tile[1]
        tile_pairs.add((top_right, bottom_left, bottom_right, top_left))
    
    # Check for each tile if there is a corresponding tile to match
    for tile in tiles:
        top_left, top_right = tile[0]
        bottom_left, bottom_right = tile[1]
        if (bottom_right, top_left, top_left, bottom_left) not in tile_pairs:
            return "NO"
    
    return "YES"

t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    
    for _ in range(n):
        top = list(map(int, input().split()))
        bottom = list(map(int, input().split()))
        tiles.append((top, bottom))
    
    result = can_construct_square(n, m, tiles)
    results.append(result)

print("\n".join(results))