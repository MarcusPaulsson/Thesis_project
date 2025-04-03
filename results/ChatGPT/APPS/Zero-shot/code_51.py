def can_have_no_winner(n, k, d1, d2):
    # Calculate total wins and remaining wins
    total_wins = n
    wins_played = k
    
    # Wins needed for each team to be equal
    required_wins_per_team = (total_wins - wins_played) % 3
    
    # If the remaining wins are less than 0, return "no"
    if required_wins_per_team < 0:
        return "no"
    
    # The difference must be feasible with the differences d1 and d2
    if (d1 + d2) % 2 != required_wins_per_team % 2:
        return "no"
    
    # Calculate the min and max possible wins for each team
    min_wins_team1 = (wins_played - d1 - d2) // 2
    max_wins_team1 = (wins_played + d1 + d2) // 2
    
    # Check if there exists a valid scenario for equal distribution
    if min_wins_team1 < 0 or max_wins_team1 > wins_played:
        return "no"
    
    return "yes"

# Read the number of test cases
t = int(input())
results = []
for _ in range(t):
    n, k, d1, d2 = map(int, input().split())
    results.append(can_have_no_winner(n, k, d1, d2))

# Print all results
print("\n".join(results))