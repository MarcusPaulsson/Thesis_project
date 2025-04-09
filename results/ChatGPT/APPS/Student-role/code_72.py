def max_intersection_length(n, segments):
    # Extract the left and right endpoints of the segments
    lefts = [seg[0] for seg in segments]
    rights = [seg[1] for seg in segments]

    # Precompute the maximum left endpoint and minimum right endpoint
    max_left = [0] * n
    min_right = [0] * n

    max_left[0] = lefts[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], lefts[i])

    min_right[n - 1] = rights[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], rights[i])

    # Calculate the maximum possible length of the intersection after removing one segment
    max_length = 0
    for i in range(n):
        if i == 0:
            l = max_left[1]
            r = min_right[1]
        elif i == n - 1:
            l = max_left[n - 2]
            r = min_right[n - 2]
        else:
            l = max(max_left[i - 1], lefts[i + 1])
            r = min(min_right[i + 1], rights[i - 1])

        if r >= l:
            max_length = max(max_length, r - l)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_intersection_length(n, segments)
print(result)