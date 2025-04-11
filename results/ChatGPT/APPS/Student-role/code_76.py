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
            if top_right != bottom_left:
                half_tiles[(top_left, bottom_left)] = half_tiles.get((top_left, bottom_left), 0) + 1
            if top_left != bottom_right:
                half_tiles[(top_right, bottom_right)] = half_tiles.get((top_right, bottom_right), 0) + 1
        
        if len(half_tiles) == 0:
            results.append("NO")
            continue
        
        can_form = False
        for count in half_tiles.values():
            if count >= 2:
                can_form = True
                break
        
        results.append("YES" if can_form else "NO")
    
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

# Print results
for result in results:
    print(result)