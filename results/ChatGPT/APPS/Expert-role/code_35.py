def is_valid_flag(n, m, field):
    colors = set()
    stripe_height = n // 3

    if n % 3 != 0:
        return "NO"

    # Check horizontal stripes
    for i in range(3):
        stripe = field[i * stripe_height:(i + 1) * stripe_height]
        if len(set(row for row in stripe)) != 1:
            return "NO"
        colors.add(stripe[0][0])

    if len(colors) != 3:
        return "NO"

    # Check if all rows in each stripe are the same
    for i in range(3):
        for j in range(stripe_height):
            if field[i * stripe_height + j] != stripe[0]:
                return "NO"

    return "YES"

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(is_valid_flag(n, m, field))