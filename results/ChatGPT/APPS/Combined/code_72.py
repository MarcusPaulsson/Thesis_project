def max_intersection_length(n, segments):
    lefts = [segments[i][0] for i in range(n)]
    rights = [segments[i][1] for i in range(n)]
    
    max_left = max(lefts)
    min_right = min(rights)

    second_max_left = -1
    second_min_right = float('inf')

    for i in range(n):
        if lefts[i] != max_left:
            second_max_left = max(second_max_left, lefts[i])
        if rights[i] != min_right:
            second_min_right = min(second_min_right, rights[i])

    max_length = 0
    for i in range(n):
        current_left = second_max_left if lefts[i] == max_left else max_left
        current_right = second_min_right if rights[i] == min_right else min_right
        
        intersection_length = max(0, current_right - current_left)
        max_length = max(max_length, intersection_length)

    return max_length