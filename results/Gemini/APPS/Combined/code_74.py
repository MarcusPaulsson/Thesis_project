def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    counts = [0] * (n + 1)
    unique_chars = set(s)
    if len(unique_chars) == 1:
        for i in range(n + 1):
            counts[i] = 1
            for j in range(1, i + 1):
                counts[i] = counts[i] * (n - j + 1) // j
    else:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(i + 1):
                dp[i][0] = 1
                if j > 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        counts = [dp[n][i] for i in range(n + 1)]

    total_subsequences = sum(counts)

    if total_subsequences < k:
        print(-1)
        return

    cost = 0
    for length in range(n, -1, -1):
        num_subsequences_of_length = counts[length]

        if k > num_subsequences_of_length:
            cost += num_subsequences_of_length * (n - length)
            k -= num_subsequences_of_length
        else:
            cost += k * (n - length)
            k = 0
            break

    print(cost)

solve()