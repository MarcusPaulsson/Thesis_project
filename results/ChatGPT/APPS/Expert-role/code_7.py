def min_coins_to_win(t, test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        voters = case[1]
        
        # Sort voters by the number of required supporters in descending order
        voters.sort(key=lambda x: (-x[0], x[1]))  # Sort by m_i descending and then by p_i ascending

        min_coins = 0
        bought_votes = 0

        # Iterate through the voters and calculate the minimum coins needed
        for i in range(n):
            m_i, p_i = voters[i]
            # If the number of votes we have is less than required for this voter
            if bought_votes < m_i:
                # We need to buy this voter's vote
                min_coins += p_i
                bought_votes += 1  # Now we count this voter as a supporter

            # Update the number of bought votes
            bought_votes += 1  # This voter now votes for us

        results.append(min_coins)

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    voters = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, voters))

# Get results
results = min_coins_to_win(t, test_cases)

# Print results
for res in results:
    print(res)