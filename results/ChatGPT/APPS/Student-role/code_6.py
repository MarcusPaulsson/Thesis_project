def close_spots(test_cases):
    results = []
    
    for n, m, tracks in test_cases:
        # We can close the last `k` spots where k = min(n, 4*n//7)
        k = min(n, 4 * n // 7)
        spots_to_close = list(range(n - k + 1, n + 1))
        
        results.append((k, spots_to_close))
    
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    n, m = map(int, input().split())
    tracks = [tuple(map(int, input().split())) for _ in range(m)]
    test_cases.append((n, m, tracks))

# Get results
results = close_spots(test_cases)

# Print output
for k, spots in results:
    print(k)
    if k > 0:
        print(' '.join(map(str, spots)))