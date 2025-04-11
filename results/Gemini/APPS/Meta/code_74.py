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

    
    counts = [0] * (n + 1)
    for i in range(n + 1):
        counts[i] = dp[n][i]

    total_subsequences = sum(counts)
    
    if k > total_subsequences:
        print("-1")
        return

    cost = 0
    for length in range(n, -1, -1):
        num_subsequences_of_length = counts[length]
        
        if k > num_subsequences_of_length:
            cost += (n - length) * num_subsequences_of_length
            k -= num_subsequences_of_length
        else:
            cost += (n - length) * k
            k = 0
            break

    print(cost)

solve()