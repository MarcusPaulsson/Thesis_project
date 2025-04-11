n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins for Alice
# Calculate losses for Alice
losses = 0
losses += max(0, b1 - a3)  # Bob's rock beats Alice's paper
losses += max(0, b2 - a1)  # Bob's scissors beats Alice's rock
losses += max(0, b3 - a2)  # Bob's paper beats Alice's scissors

min_wins = n - losses

print(min_wins, max_wins)