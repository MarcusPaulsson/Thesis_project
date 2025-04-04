def can_construct_symmetric_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # We need to find pairs of tiles that can form symmetric positions
        possible = False
        top_right_left_bottom = {}
        
        for tile in tiles:
            a, b = tile[0]
            c, d = tile[1]
            # Store the pair (b, c) as a key to check for symmetry
            top_right_left_bottom[(b, c)] = (a, d)
        
        # Now we need to check if we can find a symmetric pair
        for (b, c), (a, d) in top_right_left_bottom.items():
            if (c, b) in top_right_left_bottom:
                possible = True
                break
        
        results.append("YES" if possible else "NO")

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
results = can_construct_symmetric_square(t, test_cases)

# Print results
for result in results:
    print(result)