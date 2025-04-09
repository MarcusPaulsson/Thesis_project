def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = max(0, dp[i - 1][0] + a[i - 1])
        dp[i][1] = max(0, max(dp[i - 1][0] + a[i - 1] * x, dp[i - 1][1] + a[i - 1] * x))
        dp[i][2] = max(0, max(dp[i - 1][1] + a[i - 1], dp[i - 1][2] + a[i - 1]))
        ans = max(ans, max(dp[i]))

    print(ans)


solve()