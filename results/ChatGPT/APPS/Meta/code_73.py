def can_complete_wall(n, heights):
    max_height = max(heights)
    total_bricks_needed = 0
    
    for height in heights:
        total_bricks_needed += max_height - height
    
    # Check if the total number of bricks needed is even
    return "YES" if total_bricks_needed % 2 == 0 else "NO"

# Input reading
n = int(input())
heights = list(map(int, input().split()))

# Output the result
print(can_complete_wall(n, heights))