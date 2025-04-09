n = int(input())
f = list(map(int, input().split()))

# Find the friends who want to give gifts and those who are still open
givers = set(range(1, n + 1)) - set(f)
receivers = set(i + 1 for i in range(n)) - set(i + 1 for i in range(n) if f[i] != 0)

# Convert to list for easier manipulation
givers = list(givers)
receivers = list(receivers)

# Assign gifts to friends who were unsure
for i in range(n):
    if f[i] == 0:
        f[i] = givers.pop()

# Output the result
print(' '.join(map(str, f)))