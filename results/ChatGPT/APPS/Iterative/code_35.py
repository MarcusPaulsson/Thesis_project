def is_valid_flag(n, m, grid):
    # Check for horizontal stripes
    if n % 3 != 0 or n < 3:
        return "NO"

    stripe_height = n // 3
    colors = set()
    
    for i in range(0, n, stripe_height):
        current_color = grid[i][0]
        if current_color in colors or any(grid[j] != current_color * m for j in range(i, i + stripe_height)):
            return "NO"
        colors.add(current_color)

    # Check for vertical stripes
    if m % 3 != 0 or m < 3:
        return "NO"

    stripe_width = m // 3
    colors.clear()
    
    for i in range(0, m, stripe_width):
        current_color = grid[0][i]
        if current_color in colors or any(grid[j][k] != current_color for j in range(n) for k in range(i, i + stripe_width)):
            return "NO"
        colors.add(current_color)

    return "YES"

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
print(is_valid_flag(n, m, grid))