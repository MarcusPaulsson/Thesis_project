def can_complete_wall(n, heights):
    max_height = max(heights)
    total_bricks_needed = sum(max_height - height for height in heights)
    
    # Check if the total number of bricks needed is even
    return total_bricks_needed % 2 == 0

# Read input
n = int(input())
heights = list(map(int, input().split()))

# Output result
print("YES" if can_complete_wall(n, heights) else "NO")