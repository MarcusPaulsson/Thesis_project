def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]
    
    # Precompute the maximum left and minimum right excluding each segment
    max_left = [0] * n
    min_right = [0] * n
    
    max_left[0] = lefts[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], lefts[i])
    
    min_right[n - 1] = rights[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], rights[i])
    
    max_length = 0
    
    for i in range(n):
        if i == 0:
            left = max_left[1]
            right = min_right[1]
        elif i == n - 1:
            left = max_left[n - 2]
            right = min_right[n - 2]
        else:
            left = max(max_left[i - 1], lefts[i + 1])
            right = min(min_right[i + 1], rights[i - 1])
        
        length = max(0, right - left)
        max_length = max(max_length, length)
    
    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))