def can_construct_symmetric_square(t, test_cases):
    results = []
    
    for n, m, tiles in test_cases:
        if m % 2 != 0:
            results.append("NO")
            continue
        
        can_form = False
        top_right_bottom_left_pairs = set()
        
        for top_left, top_right, bottom_left, bottom_right in tiles:
            top_right_bottom_left_pairs.add((top_right, bottom_left))
            if top_left == bottom_right:
                can_form = True
        
        if can_form or any((bottom_left, top_right) in top_right_bottom_left_pairs for _, top_right, bottom_left, _ in tiles):
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
        top = list(map(int, input().split()))
        bottom = list(map(int, input().split()))
        tiles.append((top[0], top[1], bottom[0], bottom[1]))  # Store as a tuple
    test_cases.append((n, m, tiles))

results = can_construct_symmetric_square(t, test_cases)
for result in results:
    print(result)