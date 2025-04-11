n = int(input())
q = list(map(int, input().split()))

# Initialize the permutation array
p = [0] * n

# Calculate the first element p[0] based on the differences
p[0] = 0  # We can start from any arbitrary value, we'll adjust later

# Build the permutation based on the differences
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Normalize the permutation to be in the range [1, n]
min_p = min(p)
offset = 1 - min_p

for i in range(n):
    p[i] += offset

# Check if the resulting permutation is valid
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(' '.join(map(str, p)))
else:
    print(-1)