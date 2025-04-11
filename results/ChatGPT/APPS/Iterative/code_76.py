def can_construct_symmetric_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # Check for pairs of tiles that can form a symmetric structure
        tile_set = set()
        can_form_symmetric = False
        
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            tile_set.add((top_left, top_right, bottom_left, bottom_right))
            # Check for the symmetric counterpart
            if (top_right, top_left, bottom_right, bottom_left) in tile_set:
                can_form_symmetric = True
        
        results.append("YES" if can_form_symmetric else "NO")
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for _ in range(n):
        top = tuple(map(int, input().split()))
        bottom = tuple(map(int, input().split()))
        tiles.append((top, bottom))
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_symmetric_square(t, test_cases)

# Print results
for result in results:
    print(result)