def can_construct_square(n, m, tiles):
    if m % 2 != 0:
        return "NO"
    
    tile_dict = {}
    for tile in tiles:
        top_left, top_right = tile[0]
        bottom_left, bottom_right = tile[1]
        
        # Check symmetry conditions
        if (top_right, bottom_left) not in tile_dict:
            tile_dict[(top_left, top_right)] = (bottom_left, bottom_right)
    
    for (top_left, top_right), (bottom_left, bottom_right) in tile_dict.items():
        if top_right == bottom_left and top_left == bottom_right:
            return "YES"
    
    return "NO"

t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for _ in range(n):
        tile_top = tuple(map(int, input().split()))
        tile_bottom = tuple(map(int, input().split()))
        tiles.append((tile_top, tile_bottom))
    
    results.append(can_construct_square(n, m, tiles))

print("\n".join(results))