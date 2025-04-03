def minimum_coins_to_win(t, test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        voters = case[1]
        
        # Sort voters by the number of required votes to get their vote
        voters.sort(key=lambda x: (x[0], x[1]))
        
        # Initialize a list to track how many voters can be convinced
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No cost to convince 0 voters
        
        for m, p in voters:
            # We go backwards to avoid overwriting results of the current iteration
            for j in range(n, m, -1):
                dp[j] = min(dp[j], dp[j - m] + p)
        
        # The result for this test case is the minimum cost to convince n voters
        results.append(min(dp[n], sum(p for _, p in voters)))
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    voters = []
    for _ in range(n):
        m, p = map(int, data[index].split())
        voters.append((m, p))
        index += 1
    test_cases.append((n, voters))

results = minimum_coins_to_win(t, test_cases)

# Printing output
for result in results:
    print(result)