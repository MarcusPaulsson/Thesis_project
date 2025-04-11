def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    max_left = max(lefts)
    min_right = min(rights)

    # Precompute the second max and second min
    sorted_lefts = sorted(lefts)
    sorted_rights = sorted(rights)

    second_max_left = sorted_lefts[-2] if n > 1 else float('-inf')
    second_min_right = sorted_rights[1] if n > 1 else float('inf')

    max_length = 0

    for i in range(n):
        l, r = segments[i]
        if l == max_left:
            current_left = second_max_left
        else:
            current_left = max_left
        
        if r == min_right:
            current_right = second_min_right
        else:
            current_right = min_right
        
        intersection_length = max(0, current_right - current_left)
        max_length = max(max_length, intersection_length)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(max_intersection_length(n, segments))