def is_valid_flag(n, m, flag):
    colors = {'R', 'G', 'B'}
    
    # Check horizontal stripes
    def check_horizontal():
        stripe_height = n // 3
        if n % 3 != 0:
            return False
        for i in range(3):
            stripe_color = flag[i * stripe_height][0]
            if stripe_color not in colors:
                return False
            if any(flag[j][k] != stripe_color for j in range(i * stripe_height, (i + 1) * stripe_height) for k in range(m)):
                return False
        return len(set(flag[i * stripe_height][0] for i in range(3))) == 3

    # Check vertical stripes
    def check_vertical():
        stripe_width = m // 3
        if m % 3 != 0:
            return False
        for i in range(3):
            stripe_color = flag[0][i * stripe_width]
            if stripe_color not in colors:
                return False
            if any(flag[j][k] != stripe_color for j in range(n) for k in range(i * stripe_width, (i + 1) * stripe_width)):
                return False
        return len(set(flag[0][i * stripe_width] for i in range(3))) == 3

    return "YES" if check_horizontal() or check_vertical() else "NO"

# Input reading
n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, flag))