n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

def is_valid_flag(field, n, m):
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0:
        return "NO"
    
    colors = set()
    for i in range(3):
        start_row = i * stripe_height
        color = field[start_row][0]
        if color not in 'RGB' or color in colors:
            return "NO"
        colors.add(color)
        for j in range(stripe_height):
            if field[start_row + j] != color * m:
                return "NO"

    return "YES" if len(colors) == 3 else "NO"

# Check for vertical stripes
def is_valid_vertical_flag(field, n, m):
    stripe_width = m // 3
    if m % 3 != 0:
        return "NO"
    
    colors = set()
    for i in range(3):
        start_col = i * stripe_width
        color = field[0][start_col]
        if color not in 'RGB' or color in colors:
            return "NO"
        colors.add(color)
        for j in range(m):
            for k in range(n):
                if field[k][start_col + j] != color:
                    return "NO"

    return "YES" if len(colors) == 3 else "NO"

# Check both orientations
result = is_valid_flag(field, n, m) if n % 3 == 0 else "NO"
if result == "NO":
    result = is_valid_vertical_flag(field, n, m) if m % 3 == 0 else "NO"

print(result)