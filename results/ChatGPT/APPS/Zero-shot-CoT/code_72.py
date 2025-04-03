def maximal_intersection_length(n, segments):
    # Separate the segments into left and right endpoints
    l = [segments[i][0] for i in range(n)]
    r = [segments[i][1] for i in range(n)]
    
    # Precompute the max of left endpoints and min of right endpoints
    max_left = [0] * n
    min_right = [0] * n
    
    max_left[0] = l[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], l[i])
    
    min_right[n - 1] = r[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], r[i])
    
    max_length = 0
    
    for i in range(n):
        if i == 0:
            left_bound = max_left[1]
            right_bound = min_right[1]
        elif i == n - 1:
            left_bound = max_left[n - 2]
            right_bound = min_right[n - 2]
        else:
            left_bound = max(max_left[i - 1], l[i + 1])
            right_bound = min(min_right[i + 1], r[i - 1])
        
        intersection_length = max(0, right_bound - left_bound)
        max_length = max(max_length, intersection_length)
    
    return max_length

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(maximal_intersection_length(n, segments))