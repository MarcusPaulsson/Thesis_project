def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        half_tiles = {}
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            # Check if we have the necessary symmetry
            if (top_right, bottom_left) not in half_tiles:
                half_tiles[(top_left, top_right)] = (bottom_left, bottom_right)
            if (bottom_right, bottom_left) not in half_tiles:
                half_tiles[(bottom_left, bottom_right)] = (top_right, top_left)
        
        # Need at least one pair that matches the symmetry requirement
        can_construct = any((k[1] == v[0] and v[1] == k[0]) for k, v in half_tiles.items())
        
        if can_construct:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
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
results = can_construct_square(t, test_cases)
for result in results:
    print(result)