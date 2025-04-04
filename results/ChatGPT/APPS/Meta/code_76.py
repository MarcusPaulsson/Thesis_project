def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        can_form_symmetry = False
        # Check if any tile can form symmetric pairs
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            if top_right == bottom_left:
                can_form_symmetry = True
                break
        
        if can_form_symmetry:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input and prepare data
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

# Get results and print them
results = can_construct_square(t, test_cases)
for result in results:
    print(result)