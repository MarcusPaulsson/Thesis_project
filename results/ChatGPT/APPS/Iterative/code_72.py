def max_intersection_length(n, segments):
    # Extract left and right endpoints
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]
    
    # Calculate the maximum and second maximum of lefts and rights
    max_left = max(lefts)
    second_max_left = sorted(lefts)[-2] if n > 2 else float('-inf')
    
    max_right = max(rights)
    second_max_right = sorted(rights)[-2] if n > 2 else float('inf')
    
    max_length = 0
    
    for i in range(n):
        l_i, r_i = segments[i]
        
        # Determine the effective left and right after removing segment i
        effective_left = max(max_left if l_i != max_left else second_max_left, l_i)
        effective_right = min(max_right if r_i != max_right else second_max_right, r_i)
        
        # Calculate the intersection length
        intersection_length = max(0, effective_right - effective_left)
        max_length = max(max_length, intersection_length)
    
    return max_length

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_intersection_length(n, segments)
print(result)