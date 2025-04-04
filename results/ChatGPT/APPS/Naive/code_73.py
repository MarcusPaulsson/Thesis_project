def can_complete_wall(n, heights):
    max_height = max(heights)
    total_bricks_needed = sum(max_height - h for h in heights)
    
    # Check if the heights can be equalized
    # We can use the formula for the total difference
    total_diff = 0
    for i in range(1, n):
        if heights[i] < heights[i - 1]:
            total_diff += heights[i - 1] - heights[i]

    # If the total number of bricks needed is even and we can fill the gaps
    return "YES" if total_bricks_needed % 2 == 0 and total_diff == 0 else "NO"

# Input reading
n = int(input().strip())
heights = list(map(int, input().strip().split()))

# Output the result
print(can_complete_wall(n, heights))