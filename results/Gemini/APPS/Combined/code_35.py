def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    def check_horizontal():
        if n % 3 != 0:
            return False
        stripe_height = n // 3
        colors = []
        for i in range(3):
            color = grid[i * stripe_height][0]
            for r in range(i * stripe_height, (i + 1) * stripe_height):
                for c in range(m):
                    if grid[r][c] != color:
                        return False
            colors.append(color)
        if len(set(colors)) != 3:
            return False
        return True

    def check_vertical():
        if m % 3 != 0:
            return False
        stripe_width = m // 3
        colors = []
        for i in range(3):
            color = grid[0][i * stripe_width]
            for r in range(n):
                for c in range(i * stripe_width, (i + 1) * stripe_width):
                    if grid[r][c] != color:
                        return False
            colors.append(color)
        if len(set(colors)) != 3:
            return False
        return True

    if check_horizontal() or check_vertical():
        print("YES")
    else:
        print("NO")

solve()