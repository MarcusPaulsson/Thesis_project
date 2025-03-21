def minimum_coins_to_win(t, test_cases):
    results = []
    
    for n, voters in test_cases:
        # Sort voters based on the required votes they need to convince them (m_i)
        voters.sort(key=lambda x: (x[0], x[1]))  # Sort by m_i first, then by p_i
        
        # To keep track of the minimum cost
        min_cost = [float('inf')] * (n + 1)  # min_cost[i] = minimum cost to convince i voters
        min_cost[0] = 0  # Cost to convince 0 voters is 0
        
        for m_i, p_i in voters:
            # We will consider this voter and update the cost for all possible numbers of convinced voters
            for j in range(n, m_i - 1, -1):
                min_cost[j] = min(min_cost[j], min_cost[j - m_i] + p_i)
        
        # The answer for this test case is the minimum cost to convince all n voters
        results.append(min_cost[n])
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    voters = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, voters))

# Get results
results = minimum_coins_to_win(t, test_cases)

# Print results
for result in results:
    print(result)