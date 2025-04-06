n = int(input())
q = list(map(int, input().split()))

# Initialize the permutation array
p = [0] * n

# Compute p_1 using the prefix sum of q
for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Normalize the permutation to make it start from 1
min_val = min(p)
offset = 1 - min_val

# Create the final permutation
p = [x + offset for x in p]

# Check if the permutation is valid
if len(set(p)) == n and all(1 <= x <= n for x in p):
    print(" ".join(map(str, p)))
else:
    print(-1)