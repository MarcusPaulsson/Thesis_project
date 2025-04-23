def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    # Precompute prefix and suffix max/min values
    prefix_max_left = [0] * n
    suffix_max_left = [0] * n
    prefix_min_right = [0] * n
    suffix_min_right = [0] * n

    prefix_max_left[0] = lefts[0]
    for i in range(1, n):
        prefix_max_left[i] = max(prefix_max_left[i - 1], lefts[i])

    suffix_max_left[n - 1] = lefts[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_max_left[i] = max(suffix_max_left[i + 1], lefts[i])

    prefix_min_right[0] = rights[0]
    for i in range(1, n):
        prefix_min_right[i] = min(prefix_min_right[i - 1], rights[i])

    suffix_min_right[n - 1] = rights[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_min_right[i] = min(suffix_min_right[i + 1], rights[i])

    max_length = 0

    for i in range(n):
        if i == 0:
            max_left = suffix_max_left[1]
            min_right = suffix_min_right[1]
        elif i == n - 1:
            max_left = prefix_max_left[n - 2]
            min_right = prefix_min_right[n - 2]
        else:
            max_left = max(prefix_max_left[i - 1], suffix_max_left[i + 1])
            min_right = min(prefix_min_right[i - 1], suffix_min_right[i + 1])

        intersection_length = max(0, min_right - max_left)
        max_length = max(max_length, intersection_length)

    return max_length