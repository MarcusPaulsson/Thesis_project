n, k = map(int, input().split())
a = list(map(int, input().split()))

solved = 0

# Solve from the left
while solved < n and a[solved] <= k:
    solved += 1

# Solve from the right
while solved < n and a[n - 1 - (solved - 1)] <= k:
    solved += 1

# Adjust if both ends contributed to the solved count
if solved > n:
    solved = n

print(solved)