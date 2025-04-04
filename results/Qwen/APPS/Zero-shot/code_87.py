def max_projects(n, r, projects):
    dp = [0] * (r + 1)
    for a, b in projects:
        for i in range(r, a - 1, -1):
            dp[i] = max(dp[i], dp[i - a] + 1)
    return dp[r]

n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]
print(max_projects(n, r, projects))