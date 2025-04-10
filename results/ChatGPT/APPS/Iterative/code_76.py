def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        # Check for symmetric pairs
        can_form_symmetric = False
        for i in range(n):
            for j in range(n):
                if tiles[i][1][0] == tiles[j][0][1] and tiles[i][1][1] == tiles[j][0][0]:
                    can_form_symmetric = True
                    break
            if can_form_symmetric:
                break
        
        results.append("YES" if can_form_symmetric else "NO")
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for _ in range(n):
        top = list(map(int, input().split()))
        bottom = list(map(int, input().split()))
        tiles.append((top, bottom))
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_square(t, test_cases)

# Print results
for result in results:
    print(result)