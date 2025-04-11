def is_valid_flag(n, m, field):
    # Check if the number of rows is divisible by 3
    if n % 3 != 0:
        return "NO"
    
    # Determine the height of each stripe
    stripe_height = n // 3
    
    # Check for horizontal stripes
    colors = set()
    for i in range(3):
        stripe_color = field[i * stripe_height][0]  # Get the color of the first column in the stripe
        colors.add(stripe_color)
        for j in range(stripe_height):
            if field[i * stripe_height + j] != stripe_color * m:
                return "NO"
    
    # Check if we have exactly three different colors
    if len(colors) != 3:
        return "NO"
    
    return "YES"

# Read input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output the result
print(is_valid_flag(n, m, field))