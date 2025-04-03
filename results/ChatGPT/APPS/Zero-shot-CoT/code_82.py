n, k = map(int, input().split())
problems = list(map(int, input().split()))

solved = 0

# Solve from the left
while solved < n and problems[0] <= k:
    solved += 1
    problems.pop(0)

# Solve from the right
while solved < n and problems and problems[-1] <= k:
    solved += 1
    problems.pop()

print(solved)