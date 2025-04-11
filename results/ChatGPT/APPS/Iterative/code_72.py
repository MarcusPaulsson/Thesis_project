def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    max_left = max(lefts)
    min_right = min(rights)

    # Precompute the second max left and second min right
    sorted_lefts = sorted(lefts)
    sorted_rights = sorted(rights)

    second_max_left = sorted_lefts[-2] if n > 1 else float('-inf')
    second_min_right = sorted_rights[1] if n > 1 else float('inf')

    max_length = 0

    for l, r in segments:
        current_left = second_max_left if l == max_left else max_left
        current_right = second_min_right if r == min_right else min_right

        if current_left <= current_right:
            max_length = max(max_length, current_right - current_left)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))