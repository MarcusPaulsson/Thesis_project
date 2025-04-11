def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # Check for pairs of tiles that can form the symmetric property
        can_form_symmetric = False
        tile_dict = {}
        
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            tile_dict[(top_left, top_right, bottom_left, bottom_right)] = True
            
            # Check for symmetric pairs
            if (top_right, top_left, bottom_right, bottom_left) in tile_dict:
                can_form_symmetric = True
        
        if can_form_symmetric:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Example usage:
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

results = can_construct_square(t, test_cases)
for result in results:
    print(result)