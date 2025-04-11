n = int(input())
a = list(map(int, input().split()))

d = [float('inf')] * n

# First pass: from left to right
for i in range(n):
    if a[i] == 0:
        d[i] = 0
    elif i > 0:
        d[i] = d[i - 1] + 1

# Second pass: from right to left
for i in range(n - 1, -1, -1):
    if i < n - 1:
        d[i] = min(d[i], d[i + 1] + 1)

print(' '.join(map(str, d)))