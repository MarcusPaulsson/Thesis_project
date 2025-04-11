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

    distinct_subsequences = 0
    counts = {}
    
    def count_distinct_subsequences(index, current_subsequence):
        nonlocal distinct_subsequences
        
        if index == n:
            if current_subsequence not in counts:
                counts[current_subsequence] = 1
                distinct_subsequences += 1
            return
        
        count_distinct_subsequences(index + 1, current_subsequence)
        count_distinct_subsequences(index + 1, current_subsequence + s[index])
    
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
    
    total_cost = 0
    
    for length in range(n, -1, -1):
        num_subsequences_of_length = dp[n][length] if length <= n else 0
        
        
        
        if num_subsequences_of_length > k:
            total_cost += (n - length) * k
            k = 0
            break
        else:
            total_cost += (n - length) * num_subsequences_of_length
            k -= num_subsequences_of_length
    
    if k > 0:
        print("-1")
    else:
        print(total_cost)

solve()