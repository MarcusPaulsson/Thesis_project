def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    total_subsequences = sum(dp[n])
    
    if k > total_subsequences:
        print("-1")
        return

    cost = 0
    for length in range(n, -1, -1):
        num_subsequences = dp[n][length]
        
        take = min(k, num_subsequences)
        cost += (n - length) * take
        k -= take
        
        if k == 0:
            break

    print(cost)

solve()