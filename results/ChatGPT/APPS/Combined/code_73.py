def can_complete_wall(n, heights):
    max_height = max(heights)

    # Count occurrences of each height
    height_count = {}
    for height in heights:
        if height in height_count:
            height_count[height] += 1
        else:
            height_count[height] = 1

    # Check if there are any gaps in the heights
    for height in range(max_height + 1):
        if height not in height_count:
            # If there's a height gap, check if it can be filled
            if height_count.get(height + 1, 0) < 2:
                return "NO"

    return "YES"

# Input reading
n = int(input())
heights = list(map(int, input().split()))

# Output result
print(can_complete_wall(n, heights))