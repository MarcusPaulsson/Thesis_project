def max_intersection_length(n, segments):
    left = [0] * n
    right = [0] * n
    
    for i in range(n):
        left[i], right[i] = segments[i]

    max_l = max(left)
    min_r = min(right)
    
    max_length = 0

    for i in range(n):
        current_l = max(max_l, left[i])
        current_r = min(min_r, right[i])
        
        if current_r >= current_l:
            length = current_r - current_l
        else:
            length = 0
        
        max_length = max(max_length, length)
        
        if left[i] == max_l or right[i] == min_r:
            new_l = max(l for j, l in enumerate(left) if j != i)
            new_r = min(r for j, r in enumerate(right) if j != i)
            if new_r >= new_l:
                length = new_r - new_l
            else:
                length = 0
            
            max_length = max(max_length, length)

    return max_length

n = int(input().strip())
segments = [tuple(map(int, input().strip().split())) for _ in range(n)]
print(max_intersection_length(n, segments))