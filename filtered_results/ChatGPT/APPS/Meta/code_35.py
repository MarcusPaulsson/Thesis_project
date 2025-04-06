def is_valid_flag(n, m, grid):
    # Check if there are exactly three colors
    colors = set()
    for row in grid:
        colors.update(row)
    
    if len(colors) != 3:
        return "NO"

    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0 or stripe_height == 0:
        return "NO"
    
    # Check each stripe
    seen_colors = set()
    for i in range(3):
        stripe_color = grid[i * stripe_height][0]
        if stripe_color in seen_colors:
            return "NO"
        seen_colors.add(stripe_color)
        
        for j in range(i * stripe_height, (i + 1) * stripe_height):
            if grid[j] != stripe_color * m:
                return "NO"

    return "YES"

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    result = is_valid_flag(n, m, grid)
    print(result)

main()