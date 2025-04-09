n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Create lists to store the left and right endpoints
lefts = [l for l, r in segments]
rights = [r for l, r in segments]

# Precompute the max left and min right while excluding each segment
max_left = [0] * n
min_right = [0] * n

# Fill max_left
max_left[0] = lefts[0]
for i in range(1, n):
    max_left[i] = max(max_left[i-1], lefts[i])

# Fill min_right
min_right[n-1] = rights[n-1]
for i in range(n-2, -1, -1):
    min_right[i] = min(min_right[i+1], rights[i])

# Now calculate max intersection length when excluding each segment
max_length = 0
for i in range(n):
    if i == 0:
        current_left = max_left[1]
        current_right = min_right[1]
    elif i == n-1:
        current_left = max_left[n-2]
        current_right = min_right[n-2]
    else:
        current_left = max(max_left[i-1], lefts[i+1])
        current_right = min(min_right[i+1], rights[i-1])
    
    max_length = max(max_length, max(0, current_right - current_left))

print(max_length)