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
    position = n % layer

    if direction == 0:  # Right
        x += position
        y += 0
    elif direction == 1:  # Up-right
        x += layer
        y += position
    elif direction == 2:  # Up-left
        x += layer - position
        y += layer
    elif direction == 3:  # Left
        x -= position
        y += layer
    elif direction == 4:  # Down-left
        x -= layer
        y -= position
    elif direction == 5:  # Down-right
        x -= layer - position
        y -= layer

    return (x, y)

n = int(input())
x, y = hexagonal_coordinates(n)
print(x, y)