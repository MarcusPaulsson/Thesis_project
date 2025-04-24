def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 1

    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    x, y = layer, 0

    if n == 0:
        return (x, y)

    directions = [
        (1, 0),   # right
        (0, 1),   # top right
        (-1, 1),  # top left
        (-1, 0),  # left
        (0, -1),  # bottom left
        (1, -1)   # bottom right
    ]

    dx, dy = directions[n % 6]
    x += dx * (n // 6 + 1)
    y += dy * (n // 6 + 1)

    for i in range(n % 6):
        dx, dy = directions[i]
        x += dx
        y += dy

    return (x, y)

n = int(input().strip())
x, y = hexagonal_coordinates(n)
print(x, y)