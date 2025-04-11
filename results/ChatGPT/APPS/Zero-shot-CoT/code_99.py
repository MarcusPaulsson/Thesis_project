n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins for Alice
# Calculate losses for Alice
alice_losses = 0
alice_losses += max(0, b1 - a3)  # Bob's rock beats Alice's paper
alice_losses += max(0, b2 - a1)  # Bob's scissors beat Alice's rock
alice_losses += max(0, b3 - a2)  # Bob's paper beats Alice's scissors

# Minimum wins for Alice
min_wins = n - alice_losses

print(min_wins, max_wins)