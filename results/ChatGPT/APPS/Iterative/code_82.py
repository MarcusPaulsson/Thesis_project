n, k = map(int, input().split())
a = list(map(int, input().split()))

solved = 0

# Solve from the left
while solved < n and a[solved] <= k:
    solved += 1

# Solve from the right
while solved < n and a[n - 1 - (solved - 1)] <= k:
    solved += 1

# If we've counted a problem from both ends, we need to subtract one
if solved > 0 and a[solved - 1] <= k and solved > n:
    solved -= 1

print(solved)