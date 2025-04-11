n = int(input())
a = list(map(int, input().split()))

d = [0] * n
last_zero = -float('inf')

# Forward pass
for i in range(n):
    if a[i] == 0:
        last_zero = i
    d[i] = i - last_zero

last_zero = float('inf')

# Backward pass
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last_zero = i
    d[i] = min(d[i], last_zero - i)

print(' '.join(map(str, d)))