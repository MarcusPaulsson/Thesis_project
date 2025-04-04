def max_intersection_length(n, segments):
    segments.sort()
    max_length = 0
    for i in range(n):
        left = segments[0][0]
        right = segments[0][1]
        for j in range(1, n):
            if j == i:
                continue
            left = max(left, segments[j][0])
            right = min(right, segments[j][1])
            if left <= right:
                max_length = max(max_length, right - left)
            else:
                break
    return max_length

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(max_intersection_length(n, segments))