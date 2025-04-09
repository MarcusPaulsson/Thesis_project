n, k = map(int, input().split())
difficulties = list(map(int, input().split()))

solved = 0

# Solve from the left
while solved < n and difficulties[solved] <= k:
    solved += 1

# Solve from the right
while solved < n and difficulties[n - 1 - (solved - (n - solved))] <= k:
    solved += 1

# Avoid double counting if the leftmost and rightmost problems are solved
if solved > n:
    solved = n

print(solved)