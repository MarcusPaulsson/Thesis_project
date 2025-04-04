n, k = map(int, input().split())
problems = list(map(int, input().split()))

solved = 0

# Solve from the left
while solved < n and problems[solved] <= k:
    solved += 1

# Solve from the right
while solved < n and problems[n - 1 - (solved - 1)] <= k:
    solved += 1

# If we solved problems from both ends, we need to ensure we don't double count
if solved > n:
    solved = n

print(solved)