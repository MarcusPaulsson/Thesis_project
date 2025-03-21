def minimum_coins_to_win(t, test_cases):
    results = []
    for voters in test_cases:
        n = len(voters)
        # Create a list of voters with their m_i and p_i
        voters_list = [(m, p) for m, p in voters]
        
        # Sort voters by m_i (the number of votes they need) in descending order
        voters_list.sort(key=lambda x: x[0])
        
        # Initialize the minimum coins required
        min_coins = 0
        # A list to keep track of how many votes we can get
        votes = [False] * n
        
        # Iterate through voters in reverse order
        for i in range(n - 1, -1, -1):
            m_i, p_i = voters_list[i]
            # If we already have enough votes to satisfy this voter
            if sum(votes) >= m_i:
                votes[i] = True  # This voter will vote for us for free
            else:
                # We need to buy this voter's vote
                min_coins += p_i
                votes[i] = True  # This voter will vote for us for free after we pay

        results.append(min_coins)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    voters = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append(voters)

# Get results and print them
results = minimum_coins_to_win(t, test_cases)
for res in results:
    print(res)