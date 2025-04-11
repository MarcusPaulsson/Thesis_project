n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Precompute the maximum left and minimum right endpoints
max_left = [0] * n
min_right = [0] * n

max_left[0] = segments[0][0]
min_right[0] = segments[0][1]

for i in range(1, n):
    max_left[i] = max(max_left[i - 1], segments[i][0])
    min_right[i] = min(min_right[i - 1], segments[i][1])

max_left_rev = [0] * n
min_right_rev = [0] * n

max_left_rev[n - 1] = segments[n - 1][0]
min_right_rev[n - 1] = segments[n - 1][1]

for i in range(n - 2, -1, -1):
    max_left_rev[i] = max(max_left_rev[i + 1], segments[i][0])
    min_right_rev[i] = min(min_right_rev[i + 1], segments[i][1])

max_length = 0

for i in range(n):
    left = max(max_left[i - 1] if i > 0 else float('-inf'), max_left_rev[i + 1] if i < n - 1 else float('-inf'))
    right = min(min_right[i - 1] if i > 0 else float('inf'), min_right_rev[i + 1] if i < n - 1 else float('inf'))
    
    if left <= right:
        max_length = max(max_length, right - left)

print(max_length)