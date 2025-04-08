def is_valid_flag(n, m, flag):
    def check_horizontal_stripes():
        if n % 3 != 0:
            return False
        stripe_height = n // 3
        colors = set()
        for i in range(3):
            current_color = flag[i * stripe_height][0]
            colors.add(current_color)
            for row in flag[i * stripe_height:i * stripe_height + stripe_height]:
                if row != current_color * m:
                    return False
        return len(colors) == 3

    def check_vertical_stripes():
        if m % 3 != 0:
            return False
        stripe_width = m // 3
        colors = set()
        for i in range(3):
            current_color = flag[0][i * stripe_width]
            colors.add(current_color)
            for row in flag:
                if row[i * stripe_width:i * stripe_width + stripe_width] != current_color * stripe_width:
                    return False
        return len(colors) == 3

    return "YES" if check_horizontal_stripes() or check_vertical_stripes() else "NO"

# Reading input
n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

# Output the result
print(is_valid_flag(n, m, flag))