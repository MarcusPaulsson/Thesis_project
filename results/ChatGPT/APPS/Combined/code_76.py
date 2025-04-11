def can_construct_symmetric_square(t, test_cases):
    results = []
    
    for n, m, tiles in test_cases:
        if m % 2 != 0:
            results.append("NO")
            continue
        
        tile_map = {}
        
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            tile_map[(top_left, top_right)] = (bottom_left, bottom_right)
        
        can_form_symmetric = any(
            (top_right, top_left) in tile_map and tile_map[(top_right, top_left)] == (bottom_right, bottom_left)
            for tile in tiles
            for top_left, top_right in [tile[0]]
            for bottom_left, bottom_right in [tile[1]]
        )
        
        results.append("YES" if can_form_symmetric else "NO")
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    tiles = [((int(input().split()[0]), int(input().split()[1])), 
               (int(input().split()[0]), int(input().split()[1]))) for _ in range(n)]
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_symmetric_square(t, test_cases)

# Print results
print("\n".join(results))