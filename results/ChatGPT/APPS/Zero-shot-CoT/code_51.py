def can_all_teams_have_equal_wins(t, test_cases):
    results = []
    for n, k, d1, d2 in test_cases:
        remaining_matches = n - k
        
        # Calculate the minimum and maximum wins for team 1 and 2
        min_wins_t1 = (k - (d1 + d2)) // 2
        max_wins_t1 = (k + (d1 + d2)) // 2
        
        # Calculate the minimum and maximum wins for team 2 and 3
        min_wins_t2 = (k - (d1 + d2)) // 2
        max_wins_t2 = (k + (d1 + d2)) // 2
        
        # Check if there is a valid distribution of wins
        if (k >= d1 + d2) and (remaining_matches % 3 == 0) and (remaining_matches >= 0):
            results.append("yes")
        else:
            results.append("no")
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = can_all_teams_have_equal_wins(t, test_cases)

# Print output
print("\n".join(results))