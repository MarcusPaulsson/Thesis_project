def solve():
    n, k = map(int, input().split())
    s = input()
    
    distinct_dp = [[0] * (n + 1) for _ in range(n + 1)]
    distinct_dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            distinct_dp[i][0] = 1
            if j > 0:
                distinct_dp[i][j] = distinct_dp[i-1][j] + distinct_dp[i-1][j-1]
        
        for l in range(i):
             if s[i-1] == s[l]:
                 for j in range(1, i+1):
                     distinct_dp[i][j] -= distinct_dp[l][j-1]
                     distinct_dp[i][j] = max(0, distinct_dp[i][j])
    
    total_subsequences = sum(distinct_dp[n])
    
    if k > total_subsequences:
        print(-1)
        return

    ans = 0
    for i in range(n, -1, -1):
        num_subsequences_len_i = distinct_dp[n][i]
        
        if k > num_subsequences_len_i:
            ans += num_subsequences_len_i * (n - i)
            k -= num_subsequences_len_i
        else:
            ans += k * (n - i)
            k = 0
            break
            
    print(ans)

solve()