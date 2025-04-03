def is_valid_flag(n, m, field):
    colors = {'R', 'G', 'B'}
    
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0 or stripe_height == 0:
        return "NO"
    
    used_colors = set()
    for i in range(0, n, stripe_height):
        stripe = field[i]
        if len(set(stripe)) != 1 or stripe[0] in used_colors:
            return "NO"
        used_colors.add(stripe[0])
    
    if used_colors == colors:
        return "YES"
    
    # Check for vertical stripes
    stripe_width = m // 3
    if m % 3 != 0 or stripe_width == 0:
        return "NO"
    
    used_colors.clear()
    for j in range(0, m, stripe_width):
        stripe = [field[i][j] for i in range(n)]
        if len(set(stripe)) != 1 or stripe[0] in used_colors:
            return "NO"
        used_colors.add(stripe[0])
    
    return "YES" if used_colors == colors else "NO"

# Input reading
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, field))