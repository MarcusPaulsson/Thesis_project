def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        can_form_symmetric = False
        for i in range(n):
            a, b = tiles[i][0]
            c, d = tiles[i][1]
            for j in range(n):
                if i != j:
                    e, f = tiles[j][0]
                    g, h = tiles[j][1]
                    if b == g and c == f:
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
        top = tuple(map(int, input().split()))
        bottom = tuple(map(int, input().split()))
        tiles.append((top, bottom))
    test_cases.append((n, m, tiles))

# Get results
results = can_construct_square(t, test_cases)

# Print results
for result in results:
    print(result)