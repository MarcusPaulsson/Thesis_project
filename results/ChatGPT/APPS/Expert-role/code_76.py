def can_construct_symmetric_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # Check for pairs of tiles that can form the required symmetry
        can_form = False
        tile_map = {}
        
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            # Store tiles in a way to check symmetry easily
            tile_map[(top_left, top_right)] = (bottom_left, bottom_right)
        
        # Check if we can find a matching tile for symmetry
        for tile in tiles:
            top_left, top_right = tile[0]
            bottom_left, bottom_right = tile[1]
            if (bottom_left, bottom_right) in tile_map:
                can_form = True
                break
        
        results.append("YES" if can_form else "NO")
    
    return results

# Input reading and function calling would go here