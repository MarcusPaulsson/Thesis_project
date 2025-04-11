def is_valid_flag(n, m, field):
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0 or stripe_height == 0:
        return "NO"
    
    colors = set()
    for i in range(3):
        stripe_color = field[i * stripe_height][0]
        if stripe_color not in 'RGB' or stripe_color in colors:
            return "NO"
        colors.add(stripe_color)
        for j in range(stripe_height):
            if field[i * stripe_height + j] != stripe_color * m:
                return "NO"
    
    return "YES"

# Read input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, field))