def can_complete_wall(n, heights):
    max_height = max(heights)
    total_bricks_needed = sum(max_height - height for height in heights)
    
    return total_bricks_needed % 2 == 0

# Input reading
n = int(input().strip())
heights = list(map(int, input().strip().split()))

# Checking the condition and printing the result
print("YES" if can_complete_wall(n, heights) else "NO")