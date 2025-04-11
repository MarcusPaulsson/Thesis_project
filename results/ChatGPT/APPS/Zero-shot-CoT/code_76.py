def can_construct_square(t, test_cases):
    results = []
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        half_m = m // 2
        can_form = False
        
        for i in range(n):
            for j in range(n):
                if tiles[i][0][1] == tiles[j][1][0]:  # Check if top-right of tile i matches bottom-left of tile j
                    can_form = True
                    break
            if can_form:
                break
        
        results.append("YES" if can_form else "NO")
    
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
        tiles.append((top, bottom))
    test_cases.append((n, m, tiles))

results = can_construct_square(t, test_cases)
for result in results:
    print(result)