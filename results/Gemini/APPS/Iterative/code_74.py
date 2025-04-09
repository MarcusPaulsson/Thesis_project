def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    distinct_dp = [[0] * (n + 1) for _ in range(n + 1)]
    distinct_dp[0][0] = 1

    for i in range(1, n + 1):
        char = s[i-1]
        for j in range(i + 1):
            distinct_dp[i][0] = 1
            if j > 0:
                distinct_dp[i][j] = distinct_dp[i-1][j-1] + distinct_dp[i-1][j]
        
        for prev in range(i - 1, 0, -1):
            if s[prev - 1] == char:
                for j in range(1, i + 1):
                    distinct_dp[i][j] -= distinct_dp[prev - 1][j - 1]
                break
    
    distinct_subsequence_counts = [0] * (n + 1)
    for i in range(n + 1):
        distinct_subsequence_counts[i] = distinct_dp[n][i]
        
    total_distinct = sum(distinct_subsequence_counts)
    if total_distinct < k:
        print("-1")
        return

    cost = 0
    for length in range(n, -1, -1):
        count = distinct_subsequence_counts[length]
        
        take = min(count, k)
        cost += (n - length) * take
        k -= take
        
        if k == 0:
            break
    
    print(cost)


solve()