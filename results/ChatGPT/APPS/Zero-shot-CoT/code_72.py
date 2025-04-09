n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Precompute the min and max endpoints
prefix_min = [0] * n
prefix_max = [0] * n
suffix_min = [0] * n
suffix_max = [0] * n

prefix_min[0] = segments[0][0]
prefix_max[0] = segments[0][1]
for i in range(1, n):
    prefix_min[i] = min(prefix_min[i-1], segments[i][0])
    prefix_max[i] = max(prefix_max[i-1], segments[i][1])

suffix_min[n-1] = segments[n-1][0]
suffix_max[n-1] = segments[n-1][1]
for i in range(n-2, -1, -1):
    suffix_min[i] = min(suffix_min[i+1], segments[i][0])
    suffix_max[i] = max(suffix_max[i+1], segments[i][1])

max_length = 0
for i in range(n):
    if i == 0:
        l_intersection = suffix_min[1]
        r_intersection = suffix_max[1]
    elif i == n-1:
        l_intersection = prefix_min[n-2]
        r_intersection = prefix_max[n-2]
    else:
        l_intersection = min(prefix_min[i-1], suffix_min[i+1])
        r_intersection = max(prefix_max[i-1], suffix_max[i+1])
    
    intersection_length = max(0, r_intersection - l_intersection)
    max_length = max(max_length, intersection_length)

print(max_length)