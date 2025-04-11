def max_intersection_length(n, segments):
    left = [0] * n
    right = [0] * n

    for i in range(n):
        left[i] = segments[i][0]
        right[i] = segments[i][1]

    max_left = [0] * n
    min_right = [0] * n

    max_left[0] = left[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], left[i])

    min_right[n - 1] = right[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], right[i])

    max_length = 0

    for i in range(n):
        current_left = max_left[i - 1] if i > 0 else left[1]
        current_right = min_right[i + 1] if i < n - 1 else right[n - 2]
        
        intersection_length = max(0, current_right - current_left)
        max_length = max(max_length, intersection_length)

    return max_length

# Example usage:
# n = int(input())
# segments = [tuple(map(int, input().split())) for _ in range(n)]
# print(max_intersection_length(n, segments))