def max_perfect_teams(q, queries):
    results = []
    for c, m, x in queries:
        # The maximum number of teams cannot exceed the minimum of coders and mathematicians
        # and also cannot exceed the total number of students divided by 3
        max_teams = min(c, m, (c + m + x) // 3)
        results.append(max_teams)
    return results

# Read input
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Get results and print
results = max_perfect_teams(q, queries)
for result in results:
    print(result)