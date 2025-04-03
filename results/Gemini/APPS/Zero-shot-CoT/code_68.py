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

    subsequence_counts = [dp[n][i] for i in range(n + 1)]

    unique_subsequence_counts = [0] * (n + 1)
    last_occurrence = {}

    for i in range(n):
        char = s[i]
        if char in last_occurrence:
            index = last_occurrence[char]
            for j in range(1, i + 1):
                unique_subsequence_counts[j] = unique_subsequence_counts[j] + dp[i][j] - dp[index][j - 1]
        else:
            for j in range(1, i + 1):
                unique_subsequence_counts[j] = unique_subsequence_counts[j] + dp[i][j]
        unique_subsequence_counts[0] += 1
        last_occurrence[char] = i

    total_cost = 0
    remaining_k = k
    
    for length in range(n, -1, -1):
        count = min(remaining_k, unique_subsequence_counts[length])
        total_cost += count * (n - length)
        remaining_k -= count
        
        if remaining_k == 0:
            print(total_cost)
            return

    print(-1)

solve()