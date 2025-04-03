def max_intersection_length(n, segments):
    # Create lists to store the left and right ends of the segments
    left_ends = [segments[i][0] for i in range(n)]
    right_ends = [segments[i][1] for i in range(n)]
    
    # Compute prefix and suffix maximums and minimums
    max_left_prefix = [0] * n
    min_right_prefix = [0] * n
    max_left_suffix = [0] * n
    min_right_suffix = [0] * n

    max_left_prefix[0] = left_ends[0]
    min_right_prefix[0] = right_ends[0]
    
    for i in range(1, n):
        max_left_prefix[i] = max(max_left_prefix[i - 1], left_ends[i])
        min_right_prefix[i] = min(min_right_prefix[i - 1], right_ends[i])

    max_left_suffix[n - 1] = left_ends[n - 1]
    min_right_suffix[n - 1] = right_ends[n - 1]
    
    for i in range(n - 2, -1, -1):
        max_left_suffix[i] = max(max_left_suffix[i + 1], left_ends[i])
        min_right_suffix[i] = min(min_right_suffix[i + 1], right_ends[i])
    
    max_length = 0
    
    for i in range(n):
        if i == 0:
            max_left = max_left_suffix[1]
            min_right = min_right_suffix[1]
        elif i == n - 1:
            max_left = max_left_prefix[n - 2]
            min_right = min_right_prefix[n - 2]
        else:
            max_left = max(max_left_prefix[i - 1], max_left_suffix[i + 1])
            min_right = min(min_right_prefix[i - 1], min_right_suffix[i + 1])

        intersection_length = max(0, min_right - max_left)
        max_length = max(max_length, intersection_length)
    
    return max_length

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(max_intersection_length(n, segments))