def min_cost(n, m, k):
    # The maximum number of squares is n * m, and we want to keep n * m - k squares
    to_keep = n * m - k
    dp = [[float('inf')] * (n * m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for h in range(1, n + 1):
        for w in range(1, m + 1):
            total = h * w
            for cut in range(1, h):
                cost = w * w
                dp[h][total] = min(dp[h][total], dp[cut][total - w] + cost + dp[h - cut][total])
            for cut in range(1, w):
                cost = h * h
                dp[h][total] = min(dp[h][total], dp[h][total - h] + cost + dp[h][cut] + dp[h][w - cut])

            dp[h][total] = min(dp[h][total], dp[h][total])

    return dp[n][n * m]

t = int(input())
results = []
for _ in range(t):
    n, m, k = map(int, input().split())
    results.append(min_cost(n, m, k))

for result in results:
    print(result)