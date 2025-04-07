n = int(input())
q = list(map(int, input().split()))

# Calculate the prefix sums to get the permutation
p = [0] * n
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Normalize the permutation to be between 1 and n
min_p = min(p)
p = [x - min_p + 1 for x in p]

# Check if p is a valid permutation
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(" ".join(map(str, p)))
else:
    print(-1)