def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]

    counts = []
    for i in range(n + 1):
        counts.append(dp[n][i])

    total_subsequences = sum(counts)
    
    if total_subsequences < k:
        print("-1")
        return

    ans = 0
    for length in range(n, -1, -1):
        take = min(counts[length], k)
        ans += (n - length) * take
        k -= take

        if k == 0:
            break

    print(ans)

solve()