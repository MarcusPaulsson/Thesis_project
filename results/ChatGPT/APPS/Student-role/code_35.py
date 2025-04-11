def is_valid_flag(n, m, field):
    colors = {'R', 'G', 'B'}
    
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0 or stripe_height == 0:
        return "NO"
    
    seen_colors = set()
    for i in range(3):
        stripe = field[i * stripe_height:(i + 1) * stripe_height]
        if len(set(stripe)) != 1 or stripe[0][0] not in colors:
            return "NO"
        seen_colors.add(stripe[0][0])
    
    if seen_colors != colors:
        return "NO"
    
    return "YES"

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(is_valid_flag(n, m, field))