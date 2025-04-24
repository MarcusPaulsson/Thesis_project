def can_complete_wall(n, heights):
    max_height = max(heights)
    
    # Calculate the total number of bricks needed
    total_bricks_needed = sum(max_height - height for height in heights)
    
    # Check if the total number of bricks needed is even
    return total_bricks_needed % 2 == 0

# Input reading
n = int(input())
heights = list(map(int, input().split()))

# Output result
print("YES" if can_complete_wall(n, heights) else "NO")