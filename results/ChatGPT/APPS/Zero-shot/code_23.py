def minimum_coins_to_win(test_cases):
    results = []
    
    for voters in test_cases:
        n = len(voters)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for m, p in voters:
            for j in range(n, m - 1, -1):
                dp[j] = min(dp[j], dp[j - m] + p)
        
        answer = min(dp[j] for j in range(n + 1))
        results.append(answer)
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    voters = [tuple(map(int, input().split())) for __ in range(n)]
    test_cases.append(voters)

results = minimum_coins_to_win(test_cases)
for result in results:
    print(result)