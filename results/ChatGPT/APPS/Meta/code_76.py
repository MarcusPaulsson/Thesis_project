def can_construct_symmetric_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        top_left_bottom_right = set()
        top_right_bottom_left = set()
        
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            top_left_bottom_right.add((top_left, bottom_right))
            top_right_bottom_left.add((top_right, bottom_left))
        
        if any((x in top_right_bottom_left) for x in top_left_bottom_right):
            results.append("YES")
        else:
            results.append("NO")
    
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

# Output results
for result in results:
    print(result)