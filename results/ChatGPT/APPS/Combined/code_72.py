def maximal_intersection_length(n, segments):
    if n == 2:
        # Directly compute the length when there are only two segments
        return max(0, min(segments[0][1], segments[1][1]) - max(segments[0][0], segments[1][0]))

    # Extract left and right endpoints
    lefts = [segment[0] for segment in segments]
    rights = [segment[1] for segment in segments]

    # Initialize arrays for maximum left and minimum right values
    max_left = [0] * n
    min_right = [0] * n

    max_left[0] = lefts[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], lefts[i])
    
    min_right[n - 1] = rights[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], rights[i])
    
    # Calculate the maximal intersection length excluding each segment
    max_length = 0
    for i in range(n):
        current_max_left = max_left[i - 1] if i > 0 else max_left[1]
        current_min_right = min_right[i + 1] if i < n - 1 else min_right[n - 2]

        # Calculate the intersection length
        intersection_length = max(0, current_min_right - current_max_left)
        max_length = max(max_length, intersection_length)

    return max_length

# Read input
import sys
input = sys.stdin.read
data = input().strip().split("\n")
n = int(data[0])
segments = [tuple(map(int, line.split())) for line in data[1:]]

# Get the result and print
result = maximal_intersection_length(n, segments)
print(result)