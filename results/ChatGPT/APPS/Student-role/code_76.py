def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # Prepare to check for symmetry
        top_left = set()
        top_right = set()
        bottom_left = set()
        bottom_right = set()

        for tile in tiles:
            top_left.add(tile[0][0])
            top_right.add(tile[0][1])
            bottom_left.add(tile[1][0])
            bottom_right.add(tile[1][1])

        # Check symmetry conditions
        can_form_symmetric = False
        for tl in top_left:
            if tl in bottom_right and tl in top_right and tl in bottom_left:
                can_form_symmetric = True
                break
        
        results.append("YES" if can_form_symmetric else "NO")
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for __ in range(n):
        tile = [list(map(int, input().split())), list(map(int, input().split()))]
        tiles.append(tile)
    test_cases.append((n, m, tiles))

# Getting results
results = can_construct_square(t, test_cases)

# Printing results
for result in results:
    print(result)