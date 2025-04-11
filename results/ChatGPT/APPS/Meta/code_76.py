def can_construct_square(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        top_left = set()
        bottom_right = set()
        
        for tile in tiles:
            top_left.add((tile[0][0], tile[1][1]))
            bottom_right.add((tile[1][0], tile[0][1]))
        
        if any((a, b) in bottom_right for a, b in top_left):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Example usage
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = [tuple(tuple(map(int, input().split())) for _ in range(2)) for _ in range(n)]
    test_cases.append((n, m, tiles))

results = can_construct_square(t, test_cases)
for result in results:
    print(result)