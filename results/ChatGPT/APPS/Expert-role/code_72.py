def max_intersection_length(n, segments):
    # Extract left and right endpoints
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]
    
    # Precompute the maximum left and minimum right excluding each segment
    max_left_exclude = [0] * n
    min_right_exclude = [0] * n
    
    # Calculate prefix max for lefts and suffix min for rights
    prefix_max_left = [0] * n
    suffix_min_right = [0] * n
    
    prefix_max_left[0] = lefts[0]
    for i in range(1, n):
        prefix_max_left[i] = max(prefix_max_left[i - 1], lefts[i])
    
    suffix_min_right[n - 1] = rights[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_min_right[i] = min(suffix_min_right[i + 1], rights[i])
    
    # Calculate max_left_exclude and min_right_exclude
    for i in range(n):
        if i == 0:
            max_left_exclude[i] = prefix_max_left[1]
        elif i == n - 1:
            max_left_exclude[i] = prefix_max_left[n - 2]
        else:
            max_left_exclude[i] = max(prefix_max_left[i - 1], prefix_max_left[i + 1])
        
        if i == 0:
            min_right_exclude[i] = suffix_min_right[1]
        elif i == n - 1:
            min_right_exclude[i] = suffix_min_right[n - 2]
        else:
            min_right_exclude[i] = min(suffix_min_right[i - 1], suffix_min_right[i + 1])
    
    # Calculate the maximum intersection length after removing each segment
    max_length = 0
    for i in range(n):
        left = max_left_exclude[i]
        right = min_right_exclude[i]
        if right >= left:
            max_length = max(max_length, right - left)
    
    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))