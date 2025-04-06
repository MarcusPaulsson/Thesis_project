def is_valid_flag(n, m, field):
    # Check for horizontal stripes
    if n % 3 == 0:
        stripe_height = n // 3
        colors = set()
        for i in range(3):
            stripe = field[i * stripe_height:(i + 1) * stripe_height]
            if len(set(row for row in stripe)) != 1:
                return "NO"
            colors.add(stripe[0][0])
        if len(colors) == 3:
            return "YES"

    # Check for vertical stripes
    if m % 3 == 0:
        stripe_width = m // 3
        colors = set()
        for i in range(3):
            stripe = [row[i * stripe_width:(i + 1) * stripe_width] for row in field]
            if len(set(row for row in stripe)) != 1:
                return "NO"
            colors.add(stripe[0][0])
        if len(colors) == 3:
            return "YES"

    return "NO"

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
print(is_valid_flag(n, m, field))