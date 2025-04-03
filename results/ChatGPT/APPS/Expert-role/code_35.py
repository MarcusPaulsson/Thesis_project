def is_valid_flag(n, m, flag):
    # Check for horizontal stripes
    def check_horizontal():
        stripe_height = n // 3
        if n % 3 != 0:
            return False
        colors = set()
        for i in range(3):
            color = flag[i * stripe_height][0]
            colors.add(color)
            for j in range(i * stripe_height, (i + 1) * stripe_height):
                if flag[j] != color * m:
                    return False
        return len(colors) == 3

    # Check for vertical stripes
    def check_vertical():
        stripe_width = m // 3
        if m % 3 != 0:
            return False
        colors = set()
        for i in range(3):
            color = flag[0][i * stripe_width]
            colors.add(color)
            for j in range(m):
                for k in range(i * stripe_width, (i + 1) * stripe_width):
                    if flag[j][k] != color:
                        return False
        return len(colors) == 3

    return "YES" if check_horizontal() or check_vertical() else "NO"

# Input reading
n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, flag))