def max_intersection_length(n, segments):
    # Extract left and right endpoints
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    # Calculate the overall max left and min right
    overall_max_left = max(lefts)
    overall_min_right = min(rights)

    # Prepare to find the second max left and second min right
    sorted_lefts = sorted(lefts)
    sorted_rights = sorted(rights)

    # Find the second max left and second min right
    second_max_left = sorted_lefts[-2] if n > 1 else float('-inf')
    second_min_right = sorted_rights[1] if n > 1 else float('inf')

    max_length = 0

    for i in range(n):
        l, r = segments[i]

        # Determine the effective left and right after removing segment i
        if l == overall_max_left:
            effective_left = second_max_left
        else:
            effective_left = overall_max_left

        if r == overall_min_right:
            effective_right = second_min_right
        else:
            effective_right = overall_min_right

        # Calculate the length of the intersection
        intersection_length = max(0, effective_right - effective_left)
        max_length = max(max_length, intersection_length)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))