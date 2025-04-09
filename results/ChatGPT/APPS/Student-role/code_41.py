n = int(input())
a = list(map(int, input().split()))

d = [0] * n
last_zero = -float('inf')

# Forward pass to find distances to the nearest zero on the left
for i in range(n):
    if a[i] == 0:
        last_zero = i
        d[i] = 0
    else:
        d[i] = i - last_zero

last_zero = float('inf')

# Backward pass to find distances to the nearest zero on the right
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last_zero = i
    else:
        d[i] = min(d[i], last_zero - i)

print(' '.join(map(str, d)))