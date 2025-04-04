def rock_paper_scissors(n, alice_choices, bob_choices):
    a1, a2, a3 = alice_choices  # Alice: rock, scissors, paper
    b1, b2, b3 = bob_choices    # Bob: rock, scissors, paper

    # Maximum wins for Alice
    max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

    # Minimum wins for Alice
    # Calculate losses for Alice
    alice_losses = 0
    # Bob's rock beats Alice's scissors
    alice_losses += min(a2, b1)
    # Bob's scissors beat Alice's paper
    alice_losses += min(a3, b2)
    # Bob's paper beats Alice's rock
    alice_losses += min(a1, b3)

    # Minimum wins for Alice can be calculated as total rounds - losses
    min_wins = n - alice_losses

    return min_wins, max_wins

# Input reading
n = int(input())
alice_choices = list(map(int, input().split()))
bob_choices = list(map(int, input().split()))

# Calculate results
min_wins, max_wins = rock_paper_scissors(n, alice_choices, bob_choices)

# Output results
print(min_wins, max_wins)