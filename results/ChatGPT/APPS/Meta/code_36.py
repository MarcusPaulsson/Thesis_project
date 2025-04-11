def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 0

    # Find the layer where the nth move is located
    while moves_in_layer <= n:
        moves_in_layer += 6 * layer
        layer += 1

    layer -= 1
    moves_in_layer -= 6 * layer

    # Calculate the position in the layer
    position_in_layer = n - moves_in_layer

    # Calculate the coordinates based on the layer and position
    x, y = layer, 0

    if position_in_layer < layer:
        x -= position_in_layer
    elif position_in_layer < 2 * layer:
        x -= layer
        y += position_in_layer - layer
    elif position_in_layer < 3 * layer:
        x += position_in_layer - 2 * layer
        y += layer
    elif position_in_layer < 4 * layer:
        x += layer
        y -= position_in_layer - 3 * layer
    elif position_in_layer < 5 * layer:
        x += 5 * layer - position_in_layer
        y -= layer
    else:
        x -= layer
        y -= position_in_layer - 5 * layer

    return (x, y)

n = int(input())
x, y = hexagonal_coordinates(n)
print(x, y)