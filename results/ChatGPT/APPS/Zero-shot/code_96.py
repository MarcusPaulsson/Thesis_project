n = int(input())
q = list(map(int, input().split()))

# Initialize p array and calculate the prefix sums
p = [0] * n
p[0] = 0  # Let's assume p_1 = 0 for convenience

for i in range(1, n):
    p[i] = p[i - 1] + q[i - 1]

# Normalize p to make it a permutation of 1 to n
min_p = min(p)
p = [x - min_p + 1 for x in p]

# Check if p is a valid permutation
if sorted(p) == list(range(1, n + 1)):
    print(' '.join(map(str, p)))
else:
    print(-1)