n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Calculate maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Calculate minimum wins for Alice
# The minimum wins can be calculated by assuming the worst-case scenario
# where Alice loses as many rounds as possible.
min_wins = 0
# Bob's winning pairs
min_wins += max(0, b1 - a3)  # Bob's rock vs Alice's paper
min_wins += max(0, b2 - a1)  # Bob's scissors vs Alice's rock
min_wins += max(0, b3 - a2)  # Bob's paper vs Alice's scissors

# Total losses for Alice is the minimum wins calculated
min_wins = n - min_wins

print(min_wins, max_wins)