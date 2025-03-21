def min_coins_to_win_election(test_cases):
    results = []
    
    for n, voters in test_cases:
        voters.sort(key=lambda x: (x[0], x[1]))  # Sort by m_i first, then by p_i
        min_cost = float('inf')
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            m_i, p_i = voters[i]
            # Update the dp array in reverse to avoid using the same voter multiple times
            for j in range(n, m_i, -1):
                dp[j] = min(dp[j], dp[j - m_i] + p_i)
        
        # The answer for this case is the minimum cost to convince all voters
        min_cost = min(dp)
        results.append(min_cost)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    voters = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, voters))

# Get results
results = min_coins_to_win_election(test_cases)

# Print results
for result in results:
    print(result)