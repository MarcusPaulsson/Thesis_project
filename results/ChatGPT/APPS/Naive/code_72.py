def max_intersection_length(n, segments):
    # Initialize lists to keep track of the minimum right endpoint and maximum left endpoint
    max_l = [0] * n
    min_r = [0] * n
    
    # Fill in the max_l and min_r
    for i in range(n):
        l, r = segments[i]
        max_l[i] = l
        min_r[i] = r
    
    # Precompute the maximum left endpoint and minimum right endpoint excluding each segment
    left_max = [0] * n
    right_min = [float('inf')] * n
    
    # Calculate prefix maximum of left endpoints
    for i in range(n):
        left_max[i] = max(max_l[i], left_max[i - 1] if i > 0 else 0)
    
    # Calculate suffix maximum of left endpoints
    for i in range(n - 1, -1, -1):
        if i < n - 1:
            left_max[i] = max(left_max[i], left_max[i + 1])
    
    # Calculate prefix minimum of right endpoints
    for i in range(n):
        right_min[i] = min(min_r[i], right_min[i - 1] if i > 0 else float('inf'))
    
    # Calculate suffix minimum of right endpoints
    for i in range(n - 1, -1, -1):
        if i < n - 1:
            right_min[i] = min(right_min[i], right_min[i + 1])
    
    max_length = 0
    
    # Now calculate the maximum intersection length by removing one segment
    for i in range(n):
        l = left_max[i - 1] if i > 0 else 0
        r = right_min[i + 1] if i < n - 1 else float('inf')
        if r >= l:
            max_length = max(max_length, r - l)
    
    return max_length

# Read input
n = int(input().strip())
segments = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Calculate and output the result
print(max_intersection_length(n, segments))