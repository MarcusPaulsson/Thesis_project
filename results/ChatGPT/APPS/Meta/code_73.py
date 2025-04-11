def can_complete_wall(n, heights):
    max_height = max(heights)
    for height in heights:
        if height < max_height and (height % 2) != (max_height % 2):
            return "NO"
    return "YES"

# Input reading
n = int(input())
heights = list(map(int, input().split()))

# Output the result
print(can_complete_wall(n, heights))