def rock_paper_scissors(n, a, b):
    a_rock, a_scissors, a_paper = a
    b_rock, b_scissors, b_paper = b

    # Maximum wins for Alice
    max_wins = min(a_rock, b_scissors) + min(a_scissors, b_paper) + min(a_paper, b_rock)

    # Minimum wins for Alice
    # Calculate losses for Alice
    alice_losses = 0
    alice_losses += max(0, b_rock - a_paper)  # Bob's rock beats Alice's paper
    alice_losses += max(0, b_scissors - a_rock)  # Bob's scissors beats Alice's rock
    alice_losses += max(0, b_paper - a_scissors)  # Bob's paper beats Alice's scissors

    min_wins = n - alice_losses

    return min_wins, max_wins

# Input reading
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Get results
min_wins, max_wins = rock_paper_scissors(n, a, b)

# Output results
print(min_wins, max_wins)