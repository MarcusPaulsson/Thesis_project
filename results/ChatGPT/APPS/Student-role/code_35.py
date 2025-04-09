def is_valid_flag(n, m, grid):
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0:
        return "NO"
    
    colors = set()
    for i in range(3):
        stripe_color = grid[i * stripe_height][0]
        if stripe_color in colors:
            return "NO"
        colors.add(stripe_color)
        for j in range(stripe_height):
            if grid[i * stripe_height + j] != stripe_color * m:
                return "NO"
    
    if len(colors) != 3:
        return "NO"
    
    return "YES"

# Input reading
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, grid))