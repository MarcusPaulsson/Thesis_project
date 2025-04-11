def is_valid_flag(n, m, field):
    # Check for horizontal stripes
    if n % 3 == 0:
        stripe_height = n // 3
        colors = set()
        for i in range(3):
            stripe = field[i * stripe_height:(i + 1) * stripe_height]
            first_color = stripe[0][0]
            colors.add(first_color)
            if any(row != first_color * m for row in stripe):
                return "NO"
        if len(colors) == 3:
            return "YES"
    
    # Check for vertical stripes
    if m % 3 == 0:
        stripe_width = m // 3
        colors = set()
        for i in range(3):
            stripe = [row[i * stripe_width:(i + 1) * stripe_width] for row in field]
            first_color = stripe[0][0]
            colors.add(first_color)
            if any(row != first_color * stripe_width for row in stripe):
                return "NO"
        if len(colors) == 3:
            return "YES"
    
    return "NO"

# Input reading
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output the result
print(is_valid_flag(n, m, field))