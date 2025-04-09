n = int(input())
q = list(map(int, input().split()))

# Initialize p with the first element
p = [0] * n
p[0] = 0  # We will adjust this later

# Calculate the prefix sums to get p
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Shift p to make the minimum value start from 1
min_p = min(p)
shift = 1 - min_p

# Final permutation
for i in range(n):
    p[i] += shift

# Check if p is a valid permutation
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(" ".join(map(str, p)))
else:
    print(-1)