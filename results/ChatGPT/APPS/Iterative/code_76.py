def can_construct_symmetric_square(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:  # m must be even for a symmetric square
            results.append("NO")
            continue
        
        # Check for valid pairs
        valid_pairs = set()
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            valid_pairs.add((top_right, bottom_left))  # This must match for symmetry
        
        # We need at least one tile that can form a symmetric pair
        found_symmetric_pair = False
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            if (top_left, bottom_right) in valid_pairs:
                found_symmetric_pair = True
                break
        
        results.append("YES" if found_symmetric_pair else "NO")
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for __ in range(n):
        tile_top = list(map(int, input().split()))
        tile_bottom = list(map(int, input().split()))
        tiles.append((tile_top, tile_bottom))
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_symmetric_square(t, test_cases)

# Print results
for result in results:
    print(result)