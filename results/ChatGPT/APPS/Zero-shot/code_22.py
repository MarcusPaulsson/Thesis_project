n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Precompute the minimum right endpoint and maximum left endpoint
max_left = [0] * n
min_right = [0] * n

max_left[0] = segments[0][0]
min_right[0] = segments[0][1]

for i in range(1, n):
    max_left[i] = max(max_left[i - 1], segments[i][0])
    min_right[i] = min(min_right[i - 1], segments[i][1])

# We also need to compute the prefix and suffix for max_left and min_right
prefix_max_left = [0] * n
suffix_max_left = [0] * n
prefix_min_right = [0] * n
suffix_min_right = [0] * n

prefix_max_left[0] = segments[0][0]
prefix_min_right[0] = segments[0][1]

for i in range(1, n):
    prefix_max_left[i] = max(prefix_max_left[i - 1], segments[i][0])
    prefix_min_right[i] = min(prefix_min_right[i - 1], segments[i][1])

suffix_max_left[n - 1] = segments[n - 1][0]
suffix_min_right[n - 1] = segments[n - 1][1]

for i in range(n - 2, -1, -1):
    suffix_max_left[i] = max(suffix_max_left[i + 1], segments[i][0])
    suffix_min_right[i] = min(suffix_min_right[i + 1], segments[i][1])

max_length = 0

for i in range(n):
    if i == 0:
        left = suffix_max_left[1]
        right = suffix_min_right[1]
    elif i == n - 1:
        left = prefix_max_left[n - 2]
        right = prefix_min_right[n - 2]
    else:
        left = max(prefix_max_left[i - 1], suffix_max_left[i + 1])
        right = min(prefix_min_right[i - 1], suffix_min_right[i + 1])

    length = max(0, right - left)
    max_length = max(max_length, length)

print(max_length)