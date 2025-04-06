def is_valid_flag(n, m, field):
    # Check if the number of rows is divisible by 3 for horizontal stripes
    if n % 3 == 0:
        stripe_height = n // 3
        colors = set()
        for i in range(3):
            stripe = field[i * stripe_height:(i + 1) * stripe_height]
            # Check if all rows in the stripe are the same and collect the color
            if all(row == stripe[0] for row in stripe):
                colors.add(stripe[0][0])
            else:
                return "NO"
    # Check if the number of columns is divisible by 3 for vertical stripes
    elif m % 3 == 0:
        stripe_width = m // 3
        colors = set()
        for i in range(3):
            stripe = [row[i * stripe_width:(i + 1) * stripe_width] for row in field]
            # Check if all columns in the stripe are the same and collect the color
            if all(row == stripe[0] for row in stripe):
                colors.add(stripe[0][0])
            else:
                return "NO"
    else:
        return "NO"

    # Validate the number of unique colors used
    return "YES" if len(colors) == 3 else "NO"

# Read input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output result
print(is_valid_flag(n, m, field))