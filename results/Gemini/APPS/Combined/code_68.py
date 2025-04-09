def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

            dp[i][j] = min(dp[i][j], k)

    total_cost = 0
    for length in range(n, -1, -1):
        take = min(k, dp[n][length])
        total_cost += (n - length) * take
        k -= take

        if k == 0:
            print(total_cost)
            return

    print("-1")


solve()