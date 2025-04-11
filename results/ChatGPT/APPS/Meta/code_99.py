def rock_paper_scissors(n, a, b):
    a1, a2, a3 = a  # Alice's counts for rock, scissors, paper
    b1, b2, b3 = b  # Bob's counts for rock, scissors, paper

    # Maximum wins for Alice
    max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

    # Minimum wins for Alice
    # Calculate losses for Alice
    alice_losses = max(0, b1 - a3) + max(0, b2 - a1) + max(0, b3 - a2)
    min_wins = n - alice_losses

    return min_wins, max_wins

# Example usage:
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = rock_paper_scissors(n, a, b)
print(result[0], result[1])