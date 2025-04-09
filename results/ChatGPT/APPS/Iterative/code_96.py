n = int(input())
q = list(map(int, input().split()))

# Initialize the permutation array
p = [0] * n

# Calculate p based on q
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Find the minimum value in p
min_p = min(p)

# Adjust the array to make the smallest element 1
adjustment = 1 - min_p
for i in range(n):
    p[i] += adjustment

# Check if the permutation is valid
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(' '.join(map(str, p)))
else:
    print(-1)