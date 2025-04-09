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

    total_subsequences = sum(dp[n])
    
    if k > total_subsequences:
        print("-1")
        return

    counts = [0] * (n + 1)
    for i in range(n + 1):
        counts[i] = dp[n][i]

    cost = 0
    length = n
    while k > 0:
        if counts[length] >= k:
            cost += (n - length) * k
            k = 0
        else:
            cost += (n - length) * counts[length]
            k -= counts[length]
        length -= 1

    print(cost)

solve()