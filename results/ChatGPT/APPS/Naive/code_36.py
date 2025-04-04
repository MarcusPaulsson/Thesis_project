def get_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 0

    # Determine which layer the move n is in
    while moves_in_layer <= n:
        layer += 1
        moves_in_layer = 3 * layer * (layer + 1)  # Total moves in layer

    layer -= 1
    moves_in_layer = 3 * layer * (layer + 1)  # Moves in the last complete layer
    position_in_layer = n - moves_in_layer  # Position in the current layer

    # Calculate the coordinates based on the layer and position
    x, y = layer, 0  # Starting position for the layer

    if position_in_layer < layer:
        x -= position_in_layer
    elif position_in_layer < 2 * layer:
        x -= layer
        y += position_in_layer - layer
    else:
        x += position_in_layer - 2 * layer
        y += layer

    return (x, y)

n = int(input().strip())
x, y = get_coordinates(n)
print(x, y)