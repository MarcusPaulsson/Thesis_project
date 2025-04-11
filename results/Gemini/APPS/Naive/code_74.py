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

    counts = [[0] * (n + 1) for _ in range(n + 1)]
    counts[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            counts[i][0] = 1
            if j > 0:
                counts[i][j] = counts[i - 1][j] + counts[i - 1][j - 1]
        
        for l in range(i):
            if s[i-1] == s[l]:
                for j in range(1, i + 1):
                    counts[i][j] -= counts[l][j-1]

    total_cost = 0
    
    for length in range(n, -1, -1):
        num_subsequences = counts[n][length]
        
        if k > num_subsequences:
            total_cost += num_subsequences * (n - length)
            k -= num_subsequences
        else:
            total_cost += k * (n - length)
            k = 0
            break
    
    if k > 0:
        print("-1")
    else:
        print(total_cost)

solve()