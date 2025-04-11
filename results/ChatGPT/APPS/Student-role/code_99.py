n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins for Alice
# Calculate Bob's wins
bob_wins = min(b1, a2) + min(b2, a3) + min(b3, a1)

# Total rounds - Bob's wins gives Alice's minimum wins
min_wins = n - bob_wins

print(min_wins, max_wins)