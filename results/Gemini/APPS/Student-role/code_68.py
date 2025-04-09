def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        counts = {}
        for l in range(i - 1, -1, -1):
            if s[l] not in counts:
                dp[i][1:] = [dp[i][x] - dp[l][x - 1] for x in range(1, i + 1)]
                counts[s[l]] = True
    
    total_cost = 0
    for length in range(n, -1, -1):
        num_subsequences = dp[n][length]
        
        if k > num_subsequences:
            total_cost += (n - length) * num_subsequences
            k -= num_subsequences
        else:
            total_cost += (n - length) * k
            k = 0
            break
    
    if k > 0:
        print(-1)
    else:
        print(total_cost)
solve()