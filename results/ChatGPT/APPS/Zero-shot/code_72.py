def max_intersection_length(n, segments):
    # Separate the left and right endpoints
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    # Calculate the overall max and min of lefts and rights
    max_left = max(lefts)
    min_right = min(rights)

    # Prepare to find the maximum length of intersection when one segment is removed
    max_length = 0

    # Calculate the second maximum left and second minimum right
    if n == 2:
        return max(0, min_right - max_left)

    # Initialize second max and min values
    second_max_left = -float('inf')
    second_min_right = float('inf')

    for l in lefts:
        if l > second_max_left and l < max_left:
            second_max_left = l

    for r in rights:
        if r < second_min_right and r > min_right:
            second_min_right = r

    # Calculate the intersection lengths when removing each segment
    for i in range(n):
        l_i, r_i = segments[i]
        
        if l_i == max_left:
            new_left = second_max_left
        else:
            new_left = max_left
            
        if r_i == min_right:
            new_right = second_min_right
        else:
            new_right = min_right
        
        # Calculate the length of the intersection
        length = max(0, new_right - new_left)
        max_length = max(max_length, length)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))