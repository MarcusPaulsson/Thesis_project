def max_intersection_length(n, segments):
    # Extract left and right endpoints
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
    
    # Calculate the maximum intersection length after removing each segment
    max_length = 0
    for i in range(n):
        if i == 0:
            current_left = max_left[1]
            current_right = min_right[1]
        elif i == n - 1:
            current_left = max_left[n - 2]
            current_right = min_right[n - 2]
        else:
            current_left = max(max_left[i - 1], lefts[i + 1])
            current_right = min(min_right[i + 1], rights[i - 1])
        
        # Calculate the length of the intersection
        intersection_length = max(0, current_right - current_left)
        max_length = max(max_length, intersection_length)
    
    return max_length

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_intersection_length(n, segments)
print(result)