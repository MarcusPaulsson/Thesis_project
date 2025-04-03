def can_construct_symmetric_square(n, m, tiles):
    if m % 2 != 0:
        return "NO"
    
    left_top = set()
    right_bottom = set()
    
    for tile in tiles:
        left_top.add((tile[0][0], tile[0][1]))  # top-left corner
        right_bottom.add((tile[1][0], tile[1][1]))  # bottom-right corner
    
    # Checking if there exists a matching pair
    for lt in left_top:
        if (lt[1], lt[0]) in right_bottom:
            return "YES"
    
    return "NO"

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for __ in range(n):
        tile = [list(map(int, input().split())), list(map(int, input().split()))]
        tiles.append(tile)
    
    result = can_construct_symmetric_square(n, m, tiles)
    print(result)