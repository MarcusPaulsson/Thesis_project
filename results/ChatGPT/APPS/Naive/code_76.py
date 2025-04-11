def can_construct_symmetric_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # Check for symmetric pairs
        pairs = set()
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            pairs.add((top_right, bottom_left))
            pairs.add((bottom_right, top_left))
        
        # Check if we can form a symmetric square
        can_form = False
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            if (top_left == bottom_right and top_right == bottom_left):
                can_form = True
                break
        
        results.append("YES" if can_form else "NO")
    
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

# Process and output results
results = can_construct_symmetric_square(t, test_cases)
for result in results:
    print(result)