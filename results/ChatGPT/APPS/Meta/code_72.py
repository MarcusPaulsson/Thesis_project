def max_intersection_length(n, segments):
    # Prepare to find the maximum and second maximum right endpoints
    max_right = float('-inf')
    second_max_right = float('-inf')
    min_left = float('inf')

    # First pass to find max and second max right endpoints and min left endpoint
    for l, r in segments:
        if r > max_right:
            second_max_right = max_right
            max_right = r
        elif r > second_max_right:
            second_max_right = r
        min_left = min(min_left, l)

    # Prepare to find the maximum intersection length after removing each segment
    max_length = 0

    for l, r in segments:
        # Determine the right endpoint to consider after removing this segment
        if r == max_right:
            right_endpoint = second_max_right
        else:
            right_endpoint = max_right

        # Calculate the intersection length
        intersection_length = max(0, right_endpoint - min_left)
        max_length = max(max_length, intersection_length)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))