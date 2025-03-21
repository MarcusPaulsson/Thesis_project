def minimum_coins_to_win(t, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        voters = case[1]
        
        # Sort voters by the number of votes they need to convince others (m_i)
        voters.sort(key=lambda x: (x[0], x[1]))
        
        # Initialize a list to store the minimum cost to convince each voter
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 voters costs 0 coins
        
        for m, p in voters:
            # Traverse backwards to avoid overwriting values that are needed for this iteration
            for j in range(n, 0, -1):
                if j - 1 >= m:
                    dp[j] = min(dp[j], dp[j - 1] + p)
        
        # The answer for this test case is the minimum cost to convince all n voters
        result = min(dp[j] for j in range(n, n + 1))
        results.append(result)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    voters = []
    for _ in range(n):
        m, p = map(int, input().split())
        voters.append((m, p))
    test_cases.append((n, voters))

# Get results and print them
results = minimum_coins_to_win(t, test_cases)
for res in results:
    print(res)