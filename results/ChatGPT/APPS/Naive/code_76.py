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
        
        if top_left_bottom_right & top_right_bottom_left:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Example usage:
# t = number of test cases
# test_cases = [(n, m, tiles), ...]
# where tiles is a list of tuples representing the tile configurations