def max_intersection_length(n, segments):
    lefts = [l for l, r in segments]
    rights = [r for l, r in segments]

    overall_min = max(lefts)
    overall_max = min(rights)

    # Sort lefts and rights to find second min and max
    lefts_sorted = sorted(lefts)
    rights_sorted = sorted(rights)

    second_overall_min = lefts_sorted[-2] if n > 2 else float('-inf')
    second_overall_max = rights_sorted[-2] if n > 2 else float('inf')

    max_length = 0

    for i in range(n):
        l, r = segments[i]

        effective_min = second_overall_min if l == overall_min else overall_min
        effective_max = second_overall_max if r == overall_max else overall_max

        intersection_length = max(0, effective_max - effective_min)
        max_length = max(max_length, intersection_length)

    return max_length

# Input reading
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_intersection_length(n, segments))