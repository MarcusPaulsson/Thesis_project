def rock_paper_scissors(n, a, b):
    # Unpack Alice's and Bob's choices
    a_rock, a_scissors, a_paper = a
    b_rock, b_scissors, b_paper = b

    # Calculate maximum wins for Alice
    max_wins = min(a_rock, b_scissors) + min(a_scissors, b_paper) + min(a_paper, b_rock)

    # Calculate losses for Alice
    losses = max(0, b_rock - a_paper) + max(0, b_scissors - a_rock) + max(0, b_paper - a_scissors)

    # Minimum wins for Alice is total rounds minus losses
    min_wins = n - losses

    return min_wins, max_wins

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

# Get results
min_wins, max_wins = rock_paper_scissors(n, a, b)

# Print output
print(min_wins, max_wins)