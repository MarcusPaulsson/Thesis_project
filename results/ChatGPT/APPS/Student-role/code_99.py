n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins calculation
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins calculation
# Calculate losses
alice_losses = max(0, a1 - b3) + max(0, a2 - b1) + max(0, a3 - b2)
bob_losses = max(0, b1 - a3) + max(0, b2 - a1) + max(0, b3 - a2)

min_wins = max(0, n - alice_losses - bob_losses)

print(min_wins, max_wins)