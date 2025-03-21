def min_coins_to_win(t, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        voters = case[1]
        
        # Sort voters by the number of votes they need to convince them
        voters.sort(key=lambda x: (x[0], x[1]))  # Sort primarily by m_i, then by p_i
        
        min_cost = float('inf')
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 0 voters means 0 cost
        
        for m, p in voters:
            # We need to check from the back to avoid overwriting results
            for j in range(n, 0, -1):
                if j - 1 >= m:
                    dp[j] = min(dp[j], dp[j - 1] + p)
        
        # We need the minimum cost to ensure we have all n voters
        min_cost = min(dp[n], min_cost)
        
        results.append(min_cost)
    
    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    voters = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, voters))

results = min_coins_to_win(t, test_cases)

# Output results
for result in results:
    print(result)