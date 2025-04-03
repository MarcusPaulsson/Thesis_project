n = int(input())
q = list(map(int, input().split()))

# Initialize the permutation array
p = [0] * n
p[0] = 0  # Start from an arbitrary point, we will adjust later

# Build the prefix sums based on q
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Find the minimum value in p to adjust to a valid permutation
min_p = min(p)

# Adjust all elements to ensure the smallest value is 1
adjustment = 1 - min_p
for i in range(n):
    p[i] += adjustment

# Check if the adjusted array is a valid permutation
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(' '.join(map(str, p)))
else:
    print(-1)