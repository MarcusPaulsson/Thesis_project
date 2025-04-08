def rock_paper_scissors(n, a1, a2, a3, b1, b2, b3):
    # Calculate maximum wins for Alice
    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)
    
    # Calculate losses for Alice
    alice_losses = max(0, b1 - a3) + max(0, b2 - a1) + max(0, b3 - a2)
    
    # Calculate minimum wins for Alice
    min_wins = n - alice_losses
    
    return min_wins, max_wins

# Read input values
n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Get results
min_wins, max_wins = rock_paper_scissors(n, a1, a2, a3, b1, b2, b3)

# Print results
print(min_wins, max_wins)