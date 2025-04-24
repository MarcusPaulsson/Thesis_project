def rock_paper_scissors(n, a, b):
    a_rock, a_scissors, a_paper = a  # Alice's counts for rock, scissors, paper
    b_rock, b_scissors, b_paper = b  # Bob's counts for rock, scissors, paper

    # Calculate maximum wins for Alice
    max_wins = min(a_rock, b_paper) + min(a_scissors, b_rock) + min(a_paper, b_scissors)

    # Calculate minimum wins for Alice
    # Calculate losses for Alice
    alice_losses = max(0, b_rock - a_paper) + max(0, b_scissors - a_rock) + max(0, b_paper - a_scissors)
    min_wins = n - alice_losses

    return min_wins, max_wins

# Input reading
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Get results
result = rock_paper_scissors(n, a, b)

# Output results
print(result[0], result[1])