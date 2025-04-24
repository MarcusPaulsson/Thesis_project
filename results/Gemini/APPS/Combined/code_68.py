def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]

    counts = [dp[n][i] for i in range(n + 1)]

    if sum(counts) < k:
        print("-1")
        return

    cost = 0
    for length in range(n, -1, -1):
        if k > counts[length]:
            cost += counts[length] * (n - length)
            k -= counts[length]
        else:
            cost += k * (n - length)
            k = 0
            break

    print(cost)


solve()