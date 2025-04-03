def can_construct_symmetric_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # To construct a symmetric m x m square, we need to check if we have
        # at least one tile type that can fulfill the symmetry requirement.
        found = False
        for tile in tiles:
            # tile is a tuple of tuples: ((a, b), (c, d))
            a, b = tile[0]
            c, d = tile[1]
            if b == c:
                found = True
                break
        
        if found:
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
    for __ in range(n):
        top = tuple(map(int, input().split()))
        bottom = tuple(map(int, input().split()))
        tiles.append((top, bottom))
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_symmetric_square(t, test_cases)

# Print results
for result in results:
    print(result)