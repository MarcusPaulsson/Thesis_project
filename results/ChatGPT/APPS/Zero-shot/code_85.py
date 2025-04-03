def is_valid_flag(n, m, grid):
    colors = set()
    if n % 3 == 0:
        stripe_height = n // 3
        for i in range(3):
            colors.add(grid[i * stripe_height][0])  # Check the color of the first column in each stripe
            for j in range(stripe_height):
                if grid[i * stripe_height + j] != grid[i * stripe_height]:
                    return "NO"
    elif m % 3 == 0:
        stripe_width = m // 3
        for i in range(3):
            colors.add(grid[0][i * stripe_width])  # Check the color of the first row in each stripe
            for j in range(stripe_width):
                if any(grid[k][i * stripe_width + j] != grid[0][i * stripe_width] for k in range(n)):
                    return "NO"
    else:
        return "NO"

    return "YES" if len(colors) == 3 else "NO"

# Read input
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, grid))