def max_perfect_teams(q, queries):
    results = []
    for c, m, x in queries:
        # Maximum teams possible based on coders and mathematicians
        teams_based_on_specializations = min(c, m)
        # Maximum teams possible based on total students
        teams_based_on_total_students = (c + m + x) // 3
        # The actual maximum teams is the minimum of the two above
        max_teams = min(teams_based_on_specializations, teams_based_on_total_students)
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