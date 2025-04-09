n = int(input())
a_1, a_2, a_3 = map(int, input().split())
b_1, b_2, b_3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a_1, b_2) + min(a_2, b_3) + min(a_3, b_1)

# Minimum wins for Alice
# Calculate total draws
draws = min(a_1, b_1) + min(a_2, b_2) + min(a_3, b_3)
# Remaining rounds after draws
remaining_rounds = n - draws
# Alice's minimum wins is the remaining rounds minus Bob's wins
min_wins = max(0, remaining_rounds - (b_1 + b_2 + b_3 - (a_1 + a_2 + a_3)))

print(min_wins, max_wins)