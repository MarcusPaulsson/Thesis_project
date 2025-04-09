def is_valid_flag(n, m, grid):
    # Check for horizontal stripes
    def check_horizontal():
        stripe_height = n // 3
        if n % 3 != 0:
            return False
        colors = set()
        
        for i in range(3):
            color = grid[i * stripe_height][0]
            colors.add(color)
            for j in range(stripe_height):
                if grid[i * stripe_height + j] != color * m:
                    return False
        return len(colors) == 3

    # Check for vertical stripes
    def check_vertical():
        stripe_width = m // 3
        if m % 3 != 0:
            return False
        colors = set()
        
        for i in range(3):
            color = grid[0][i * stripe_width]
            colors.add(color)
            for j in range(stripe_width):
                for k in range(n):
                    if grid[k][i * stripe_width + j] != color:
                        return False
        return len(colors) == 3

    return check_horizontal() or check_vertical()

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

if is_valid_flag(n, m, grid):
    print("YES")
else:
    print("NO")