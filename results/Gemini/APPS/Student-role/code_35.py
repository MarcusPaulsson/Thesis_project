def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    def check_horizontal(n, m, grid):
        if n % 3 != 0:
            return False
        stripe_height = n // 3
        colors = []
        for i in range(3):
            colors.append(grid[i * stripe_height][0])
        if len(set(colors)) != 3:
            return False
        
        for i in range(n):
            expected_color_index = i // stripe_height
            expected_color = colors[expected_color_index]
            for j in range(m):
                if grid[i][j] != expected_color:
                    return False
        return True

    def check_vertical(n, m, grid):
        if m % 3 != 0:
            return False
        stripe_width = m // 3
        colors = []
        for i in range(3):
            colors.append(grid[0][i * stripe_width])
        if len(set(colors)) != 3:
            return False
        
        for j in range(m):
            expected_color_index = j // stripe_width
            expected_color = colors[expected_color_index]
            for i in range(n):
                if grid[i][j] != expected_color:
                    return False
        return True

    if check_horizontal(n, m, grid) or check_vertical(n, m, grid):
        print("YES")
    else:
        print("NO")

solve()