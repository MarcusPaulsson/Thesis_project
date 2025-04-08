def can_construct_symmetric_square(t, test_cases):
    results = []

    for n, m, tiles in test_cases:
        if m % 2 != 0:
            results.append("NO")
            continue

        tile_map = {}
        for tile in tiles:
            top_left, top_right, bottom_left, bottom_right = tile
            tile_map[(top_left, top_right)] = (bottom_left, bottom_right)

        can_construct = any((top_right, top_left) in tile_map for (top_left, top_right), (bottom_left, bottom_right) in tile_map.items())
        
        results.append("YES" if can_construct else "NO")

    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    tiles = [tuple(map(int, input().split())) + tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_symmetric_square(t, test_cases)

# Print results
for result in results:
    print(result)