def can_construct_symmetric_square(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # To check if we can form a symmetric square, we need to find pairs of tiles
        possible = False
        
        # Create a set to store the pairs
        tile_pairs = set()
        
        for i in range(n):
            top_left, top_right = tiles[2 * i]
            bottom_left, bottom_right = tiles[2 * i + 1]
            tile_pairs.add((top_right, bottom_left))  # This is the mirror requirement
        
        # Now we check if there's any tile that can match its mirror
        for i in range(n):
            top_left, top_right = tiles[2 * i]
            bottom_left, bottom_right = tiles[2 * i + 1]
            if (top_left, bottom_right) in tile_pairs:
                possible = True
                break
        
        results.append("YES" if possible else "NO")
    
    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for __ in range(n):
        top = list(map(int, input().split()))
        bottom = list(map(int, input().split()))
        tiles.append((top, bottom))
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_symmetric_square(t, test_cases)

# Print results
for result in results:
    print(result)