def max_intersection_length(n, segments):
    lefts = [segment[0] for segment in segments]
    rights = [segment[1] for segment in segments]

    max_left = [0] * n
    min_right = [0] * n

    max_left[0] = lefts[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], lefts[i])

    min_right[n - 1] = rights[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], rights[i])

    max_length = 0

    for i in range(n):
        intersection_left = max_left[i - 1] if i > 0 else max_left[1]
        intersection_right = min_right[i + 1] if i < n - 1 else min_right[n - 2]

        length = max(0, intersection_right - intersection_left)
        max_length = max(max_length, length)

    return max_length

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
result = max_intersection_length(n, segments)
print(result)