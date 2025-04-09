n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins for Alice
# Calculate Bob's potential wins:
bob_wins = min(b1, a2) + min(b2, a3) + min(b3, a1)

# Since total rounds are n, Alice's minimum wins will be:
min_wins = n - bob_wins

print(min_wins, max_wins)