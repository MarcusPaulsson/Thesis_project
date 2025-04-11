def can_complete_wall(n, heights):
    max_height = max(heights)

    # Check if all heights can be raised to the maximum height
    for height in heights:
        if height < max_height and (max_height - height) % 2 != 0:
            return "NO"
    
    return "YES"

# Input reading
n = int(input().strip())
heights = list(map(int, input().strip().split()))

# Output the result
print(can_complete_wall(n, heights))