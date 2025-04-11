n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins for Alice
# To minimize Alice's wins, we can maximize Bob's wins
# Bob wins if:
# - Bob's rock beats Alice's scissors
# - Bob's scissors beat Alice's paper
# - Bob's paper beats Alice's rock
min_wins = max(0, b1 - a2) + max(0, b2 - a3) + max(0, b3 - a1)

print(min_wins, max_wins)