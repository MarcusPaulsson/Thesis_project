def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][0] = 1
            if j > 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    counts = {}
    for char in set(s):
        counts[char] = s.count(char)

    total_cost = 0
    num_subsequences = 0

    distinct_chars = sorted(list(set(s)))
    
    
    def count_distinct_subsequences(string):
        m = len(string)
        dp = [0] * (m + 1)
        dp[0] = 1
        last_occurrence = {}

        for i in range(1, m + 1):
            dp[i] = 2 * dp[i - 1]
            if string[i - 1] in last_occurrence:
                dp[i] -= dp[last_occurrence[string[i - 1]] - 1]
            last_occurrence[string[i - 1]] = i
        return dp[m] -1
    
    
    
    
    dp2 = [[0] * (n + 1) for _ in range(n + 1)]
    dp2[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp2[i][0] = 1
            if j > 0:
                dp2[i][j] = dp2[i-1][j] + dp2[i-1][j-1]
            if dp2[i][j] > k:
              dp2[i][j] = k
    
    
    
    for length in range(n, -1, -1):
        num_possible = dp2[n][length]

        if num_subsequences + num_possible >= k:
            total_cost += (n - length) * (k - num_subsequences)
            num_subsequences = k
            break
        else:
            total_cost += (n - length) * num_possible
            num_subsequences += num_possible

    if num_subsequences < k:
        print("-1")
    else:
        print(total_cost)

solve()