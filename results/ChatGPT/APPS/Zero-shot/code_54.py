def can_win_game(queries):
    results = []
    
    for query in queries:
        n, s = query
        if 2048 in s:
            results.append("YES")
            continue
        
        total_sum = sum(x for x in s if x < 2048)
        
        if total_sum >= 2048:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
q = int(input())
queries = []

for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    queries.append((n, s))

# Get results
results = can_win_game(queries)

# Print results
for result in results:
    print(result)