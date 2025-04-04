n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

min_wins = min(a2, b1) + min(a3, b2)
max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

print(min_wins, max_wins)