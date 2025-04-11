def get_coordinates(n):
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
        (1, 0),  # right
        (0, 1),  # top-right
        (-1, 1), # top-left
        (-1, 0), # left
        (0, -1), # bottom-left
        (1, -1)  # bottom-right
    ]

    for i in range(n):
        direction = i % 6
        x += directions[direction][0]
        y += directions[direction][1]

    return (x, y)

n = int(input().strip())
x, y = get_coordinates(n)
print(x, y)