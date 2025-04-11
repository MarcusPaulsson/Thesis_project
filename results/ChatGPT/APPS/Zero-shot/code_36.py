def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 6 * layer

    while n > moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    x, y = layer, 0

    if n == 0:
        return (x, y)

    # Determine the direction and the position in the layer
    direction = n // layer
    steps = n % layer

    if direction == 0:  # right
        x += steps
    elif direction == 1:  # top-right
        x += steps
        y += steps
    elif direction == 2:  # top-left
        x -= steps
        y += steps
    elif direction == 3:  # left
        x -= steps
    elif direction == 4:  # bottom-left
        x -= steps
        y -= steps
    elif direction == 5:  # bottom-right
        x += steps
        y -= steps

    return (x, y)

n = int(input())
x, y = hexagonal_coordinates(n)
print(x, y)