def can_construct_symmetric_square(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, tiles = case
        if m % 2 != 0:
            results.append("NO")
            continue
        
        possible = False
        for i in range(n):
            for j in range(n):
                if tiles[i][0][1] == tiles[j][1][0] and tiles[i][1][1] == tiles[j][0][0]:
                    possible = True
                    break
            if possible:
                break
        
        results.append("YES" if possible else "NO")
    
    return results

# Input reading
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

# Processing and output
results = can_construct_symmetric_square(t, test_cases)
for result in results:
    print(result)