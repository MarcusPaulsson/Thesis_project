def maximal_intersection_after_removal(n, segments):
    # Separate left and right endpoints
    lefts = [seg[0] for seg in segments]
    rights = [seg[1] for seg in segments]
    
    # Calculate prefix and suffix max and min
    prefix_max_right = [0] * n
    suffix_max_right = [0] * n
    prefix_min_left = [0] * n
    suffix_min_left = [0] * n
    
    prefix_max_right[0] = rights[0]
    prefix_min_left[0] = lefts[0]
    
    for i in range(1, n):
        prefix_max_right[i] = max(prefix_max_right[i-1], rights[i])
        prefix_min_left[i] = min(prefix_min_left[i-1], lefts[i])
    
    suffix_max_right[n-1] = rights[n-1]
    suffix_min_left[n-1] = lefts[n-1]
    
    for i in range(n-2, -1, -1):
        suffix_max_right[i] = max(suffix_max_right[i+1], rights[i])
        suffix_min_left[i] = min(suffix_min_left[i+1], lefts[i])
    
    max_length = 0
    
    for i in range(n):
        if i == 0:
            max_right = suffix_max_right[1]
            min_left = suffix_min_left[1]
        elif i == n - 1:
            max_right = prefix_max_right[n - 2]
            min_left = prefix_min_left[n - 2]
        else:
            max_right = max(prefix_max_right[i-1], suffix_max_right[i+1])
            min_left = min(prefix_min_left[i-1], suffix_min_left[i+1])
        
        intersection_length = max(0, max_right - min_left)
        max_length = max(max_length, intersection_length)
    
    return max_length

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = maximal_intersection_after_removal(n, segments)
print(result)