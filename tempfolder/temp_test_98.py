def max_perfect_teams(c, m, x):
    # The maximum number of teams we can form is limited by:
    # 1. The minimum number of coders and mathematicians (at least one of each is needed)
    # 2. The total number of students divided by 3 (since each team has 3 members)
    return min(c, m, (c + m + x) // 3)

q = int(input())
results = []
for _ in range(q):
    c, m, x = map(int, input().split())
    results.append(max_perfect_teams(c, m, x))

print('\n'.join(map(str, results)))