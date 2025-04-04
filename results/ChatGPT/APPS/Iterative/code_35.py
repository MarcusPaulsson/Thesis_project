def is_valid_flag(n, m, field):
    colors = {'R', 'G', 'B'}

    # Check horizontal stripe pattern
    def check_horizontal():
        if n % 3 != 0:
            return False
        
        stripe_height = n // 3
        seen_colors = set()
        for i in range(3):
            stripe = field[i * stripe_height:(i + 1) * stripe_height]
            if len(set(''.join(row) for row in stripe)) != 1:
                return False
            color = stripe[0][0]
            if color in seen_colors or color not in colors:
                return False
            seen_colors.add(color)
        return seen_colors == colors

    # Check vertical stripe pattern
    def check_vertical():
        if m % 3 != 0:
            return False
        
        stripe_width = m // 3
        seen_colors = set()
        for i in range(3):
            stripe = [row[i * stripe_width:(i + 1) * stripe_width] for row in field]
            if len(set(''.join(stripe))) != 1:
                return False
            color = stripe[0][0]
            if color in seen_colors or color not in colors:
                return False
            seen_colors.add(color)
        return seen_colors == colors

    return check_horizontal() or check_vertical()

# Read input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output result
print("YES" if is_valid_flag(n, m, field) else "NO")