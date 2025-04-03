def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        can_form = False
        for i in range(n):
            for j in range(n):
                if tiles[i][1] == tiles[j][0]:  # top right of tile i matches bottom left of tile j
                    can_form = True
                    break
            if can_form:
                break
        
        results.append("YES" if can_form else "NO")
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    tiles = []
    for __ in range(n):
        top = list(map(int, input().split()))
        bottom = list(map(int, input().split()))
        tiles.append((top[0], top[1], bottom[0], bottom[1]))  # (tl, tr, bl, br)
    test_cases.append((n, m, tiles))

# Getting results
results = can_construct_square(t, test_cases)

# Printing output
for result in results:
    print(result)