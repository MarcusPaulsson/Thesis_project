n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins
# Calculate draws based on optimal matches
draws = min(a1, b1) + min(a2, b2) + min(a3, b3)

# Total matches minus draws gives the possible wins for Alice
min_wins = max(0, n - draws - (b1 + b2 + b3 - (a1 + a2 + a3)))

print(min_wins, max_wins)