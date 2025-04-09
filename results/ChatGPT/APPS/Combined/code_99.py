def rock_paper_scissors(n, alice_counts, bob_counts):
    a_rock, a_scissors, a_paper = alice_counts  # Alice's counts of Rock, Scissors, Paper
    b_rock, b_scissors, b_paper = bob_counts    # Bob's counts of Rock, Scissors, Paper

    # Calculate maximum wins for Alice
    max_wins = min(a_rock, b_paper) + min(a_scissors, b_rock) + min(a_paper, b_scissors)

    # Calculate losses for Alice based on Bob's optimal plays
    losses = max(0, b_rock - a_paper) + max(0, b_scissors - a_rock) + max(0, b_paper - a_scissors)

    # Minimum wins for Alice
    min_wins = n - losses

    return min_wins, max_wins

# Reading inputs
n = int(input().strip())
alice_counts = list(map(int, input().strip().split()))
bob_counts = list(map(int, input().strip().split()))

# Getting the results
min_wins, max_wins = rock_paper_scissors(n, alice_counts, bob_counts)

# Printing results
print(min_wins, max_wins)