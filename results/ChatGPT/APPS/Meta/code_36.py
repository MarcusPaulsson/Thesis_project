def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine the layer of the spiral
    layer = 0
    while n > 3 * layer * (layer + 1):
        layer += 1

    # Number of moves in the previous layer
    moves_in_previous_layer = 3 * layer * (layer - 1)
    
    # Position in the current layer
    position_in_layer = n - moves_in_previous_layer

    # Calculate the coordinates based on position in the layer
    if position_in_layer < layer:
        x, y = layer, position_in_layer
    elif position_in_layer < 2 * layer:
        x, y = layer - (position_in_layer - layer), layer
    else:
        x, y = -layer, layer - (position_in_layer - 2 * layer)

    return (x, y)

n = int(input().strip())
x, y = hexagonal_coordinates(n)
print(x, y)