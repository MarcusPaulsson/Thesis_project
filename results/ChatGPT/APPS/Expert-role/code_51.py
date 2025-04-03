def can_have_no_winner(t, test_cases):
    results = []
    for n, k, d1, d2 in test_cases:
        # Calculate the maximum wins for each team based on the differences
        a1 = (k + d1 + d2) // 2
        a2 = (k - d1 + d2) // 2
        a3 = (k + d1 - d2) // 2
        
        # Check the conditions for equal wins
        if (k + d1 + d2) % 2 != 0 or (k - d1 + d2) % 2 != 0 or (k + d1 - d2) % 2 != 0:
            results.append("no")
            continue
        
        # Check if the total wins can be balanced with the remaining games
        total_wins = a1 + a2 + a3
        remaining_games = n - k
        
        if total_wins % 3 == 0 and total_wins // 3 <= remaining_games:
            results.append("yes")
        else:
            results.append("no")
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]

# Process and output results
results = can_have_no_winner(t, test_cases)
print("\n".join(results))