def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    # Precompute the maximum left and minimum right excluding each segment
    max_left_exclude = [0] * n
    min_right_exclude = [0] * n

    max_left = float('-inf')
    for i in range(n):
        max_left_exclude[i] = max_left
        max_left = max(max_left, lefts[i])

    min_right = float('inf')
    for i in range(n - 1, -1, -1):
        min_right_exclude[i] = min_right
        min_right = min(min_right, rights[i])

    max_length = 0
    for i in range(n):
        left = max(max_left_exclude[i], lefts[i])
        right = min(min_right_exclude[i], rights[i])
        if right >= left:
            max_length = max(max_length, right - left)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(max_intersection_length(n, segments))