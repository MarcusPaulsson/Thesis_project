def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]
    
    # Precompute the maximum left and minimum right excluding each segment
    max_left = [0] * n
    min_right = [0] * n
    
    max_left[0] = lefts[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], lefts[i])
        
    min_right[n-1] = rights[n-1]
    for i in range(n-2, -1, -1):
        min_right[i] = min(min_right[i+1], rights[i])
    
    max_length = 0
    
    for i in range(n):
        if i == 0:
            current_left = max_left[1]
            current_right = min_right[1]
        elif i == n-1:
            current_left = max_left[n-2]
            current_right = min_right[n-2]
        else:
            current_left = max(max_left[i-1], lefts[i+1])
            current_right = min(min_right[i+1], rights[i-1])
        
        # Calculate the length of the intersection
        if current_right >= current_left:
            max_length = max(max_length, current_right - current_left)
    
    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result
result = max_intersection_length(n, segments)

# Output the result
print(result)