def can_construct_symmetric_square(t, test_cases):
    results = []
    
    for n, m, tiles in test_cases:
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
        
        if any(tile in top_right_bottom_left for tile in top_left_bottom_right):
            results.append("YES")
        else:
            results.append("NO")
    
    return results