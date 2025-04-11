def max_intersection_length(n, segments):
    # Initialize lists to store the left and right endpoints
    lefts = [0] * n
    rights = [0] * n
    
    for i in range(n):
        lefts[i], rights[i] = segments[i]
    
    # Calculate the maximum and second maximum left endpoint
    max_left = max(lefts)
    second_max_left = -1
    for l in lefts:
        if l != max_left:
            second_max_left = max(second_max_left, l)
    
    # Calculate the minimum and second minimum right endpoint
    min_right = min(rights)
    second_min_right = float('inf')
    for r in rights:
        if r != min_right:
            second_min_right = min(second_min_right, r)
    
    # Calculate the maximum intersection length after removing each segment
    max_length = 0
    for i in range(n):
        if lefts[i] == max_left:
            current_left = second_max_left
        else:
            current_left = max_left
        
        if rights[i] == min_right:
            current_right = second_min_right
        else:
            current_right = min_right
        
        # Calculate the intersection length
        if current_left <= current_right:
            max_length = max(max_length, current_right - current_left)
    
    return max_length

# Example usage:
# n = int(input())
# segments = [tuple(map(int, input().split())) for _ in range(n)]
# print(max_intersection_length(n, segments))