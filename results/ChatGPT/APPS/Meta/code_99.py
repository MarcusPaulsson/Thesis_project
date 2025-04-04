n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Calculate maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Calculate minimum wins for Alice
# To find the minimum wins, we want to maximize Bob's wins
# Calculate Bob's wins against Alice's moves
bob_wins = min(a1, b1) + min(a2, b2) + min(a3, b3)
alice_wins = n - bob_wins  # Total rounds minus Bob's wins gives us Alice's wins
min_wins = alice_wins

print(min_wins, max_wins)