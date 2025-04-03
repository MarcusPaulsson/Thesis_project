n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

# Maximum wins for Alice
max_wins = min(a1, b3) + min(a2, b1) + min(a3, b2)

# Minimum wins for Alice
# To minimize Alice's wins, we can maximize Bob's wins.
# Bob wins with his rocks against Alice's scissors,
# Bob wins with his scissors against Alice's paper,
# Bob wins with his paper against Alice's rock.

alice_loses = min(a2, b1) + min(a3, b2) + min(a1, b3)
min_wins = n - alice_loses

print(min_wins, max_wins)