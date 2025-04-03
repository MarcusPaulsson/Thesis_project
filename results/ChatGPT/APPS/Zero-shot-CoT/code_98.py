def max_perfect_teams(q, queries):
    results = []
    for c, m, x in queries:
        # The maximum number of teams we can form considering the constraints
        max_teams = min(c, m, (c + m + x) // 3)
        results.append(max_teams)
    return results

# Read input
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results
results = max_perfect_teams(q, queries)

# Print results
for result in results:
    print(result)