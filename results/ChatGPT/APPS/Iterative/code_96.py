n = int(input())
q = list(map(int, input().split()))

# Initialize the permutation array
p = [0] * n

# Build the permutation based on the differences
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Find the minimum value in p to normalize it to start from 1
min_p = min(p)

# Normalize the permutation to start from 1
for i in range(n):
    p[i] -= min_p - 1

# Check if the permutation is valid
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(' '.join(map(str, p)))
else:
    print(-1)