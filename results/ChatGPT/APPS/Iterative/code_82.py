n, k = map(int, input().split())
problems = list(map(int, input().split()))

solved = 0

# Solve from the left
while solved < n and problems[solved] <= k:
    solved += 1

# Solve from the right
while solved < n and problems[n - 1 - (solved - 1)] <= k:
    solved += 1

# Adjust if we have counted the same problem from both ends
if solved > n:
    solved = n

# Calculate the total unique problems solved
left_solved = 0
right_solved = 0

# Count solved problems from the left
while left_solved < n and problems[left_solved] <= k:
    left_solved += 1

# Count solved problems from the right
while right_solved < n and problems[n - 1 - right_solved] <= k:
    right_solved += 1

# Total solved problems, ensuring we don't double count
total_solved = left_solved + right_solved
if left_solved + right_solved > n:
    total_solved = n

print(total_solved)