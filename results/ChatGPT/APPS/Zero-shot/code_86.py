def get_hexagon_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine the layer (ring) of the hexagonal spiral
    layer = 0
    while n > 3 * layer * (layer + 1):
        layer += 1

    # Calculate the number of moves within the layer
    moves_in_layer = n - 3 * layer * (layer - 1)
    
    # Determine the coordinates based on the position in the layer
    x = layer
    y = 0

    if moves_in_layer <= layer:
        x -= moves_in_layer
        return (x, y)
    moves_in_layer -= layer

    if moves_in_layer <= layer:
        x = -layer
        y += moves_in_layer
        return (x, y)
    moves_in_layer -= layer

    if moves_in_layer <= layer:
        y = layer
        x += moves_in_layer
        return (x, y)
    moves_in_layer -= layer

    if moves_in_layer <= layer:
        x += layer
        y -= moves_in_layer
        return (x, y)
    moves_in_layer -= layer

    x = layer - moves_in_layer
    y = -layer
    return (x, y)

n = int(input().strip())
x, y = get_hexagon_coordinates(n)
print(x, y)