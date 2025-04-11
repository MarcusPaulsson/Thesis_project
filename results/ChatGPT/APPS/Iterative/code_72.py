def max_intersection_length(n, segments):
    left = [segments[i][0] for i in range(n)]
    right = [segments[i][1] for i in range(n)]
    
    max_left = [0] * n
    min_right = [0] * n
    
    max_left[0] = left[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], left[i])
    
    min_right[n - 1] = right[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], right[i])
    
    max_length = 0
    
    for i in range(n):
        if i == 0:
            current_left = max_left[1]
            current_right = min_right[1]
        elif i == n - 1:
            current_left = max_left[n - 2]
            current_right = min_right[n - 2]
        else:
            current_left = max(max_left[i - 1], left[i + 1])
            current_right = min(min_right[i + 1], right[i - 1])
        
        current_length = max(0, current_right - current_left)
        max_length = max(max_length, current_length)
    
    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(max_intersection_length(n, segments))