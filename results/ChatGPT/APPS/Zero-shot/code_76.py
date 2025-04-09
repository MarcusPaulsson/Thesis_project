def can_construct_symmetric_square(test_cases):
    results = []
    for n, m, tiles in test_cases:
        if m % 2 != 0:
            results.append("NO")
            continue

        top_left_values = set()
        bottom_right_values = set()
        
        for tile in tiles:
            top_left_values.add(tile[0][0])
            bottom_right_values.add(tile[1][1])

        if top_left_values & bottom_right_values:
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
    for _ in range(n):
        top_row = list(map(int, input().split()))
        bottom_row = list(map(int, input().split()))
        tiles.append((top_row, bottom_row))
    test_cases.append((n, m, tiles))

# Process each test case
results = can_construct_symmetric_square(test_cases)

# Print results
for result in results:
    print(result)