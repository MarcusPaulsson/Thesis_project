n = int(input())
a = list(map(int, input().split()))

d = [float('inf')] * n

# First pass: from left to right
last_zero = -1
for i in range(n):
    if a[i] == 0:
        last_zero = i
        d[i] = 0
    elif last_zero != -1:
        d[i] = i - last_zero

# Second pass: from right to left
last_zero = -1
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last_zero = i
    elif last_zero != -1:
        d[i] = min(d[i], last_zero - i)

print(' '.join(map(str, d)))