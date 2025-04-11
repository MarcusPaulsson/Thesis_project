def is_valid_flag(n, m, field):
    # Check for horizontal stripes
    stripe_height = n // 3
    if n % 3 != 0:
        return "NO"
    
    colors = set()
    for i in range(3):
        stripe = field[i * stripe_height:(i + 1) * stripe_height]
        if len(set(row for row in stripe)) != 1:
            return "NO"
        colors.add(stripe[0][0])
    
    if len(colors) != 3:
        return "NO"
    
    return "YES"

# Input reading
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output the result
print(is_valid_flag(n, m, field))