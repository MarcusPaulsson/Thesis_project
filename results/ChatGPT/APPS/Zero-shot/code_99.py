# Read input values
n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins calculation
max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

# Minimum wins calculation
# Calculate losses for Alice
alice_loses = 0
alice_loses += max(0, b1 - a3)  # Bob's rocks beat Alice's paper
alice_loses += max(0, b2 - a1)  # Bob's scissors beat Alice's rock
alice_loses += max(0, b3 - a2)  # Bob's paper beats Alice's scissors

min_wins = n - alice_loses

# Output the results
print(min_wins, max_wins)