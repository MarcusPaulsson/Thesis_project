def hex_spiral_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 1

    # Find the layer
    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    # Calculate the coordinates
    x, y = layer, 0
    if n == 0:
        return (x, y)

    # The starting point of the current layer is at (layer, 0)
    # Each segment of the layer is 1 step in the direction of the hexagon
    for i in range(n):
        if i < layer:
            x -= 1  # Move left
        elif i < 2 * layer:
            x -= 1  # Move left
            y += 1  # Move up
        elif i < 3 * layer:
            y += 1  # Move up
        elif i < 4 * layer:
            x += 1  # Move right
            y += 1  # Move up
        elif i < 5 * layer:
            x += 1  # Move right
        else:
            x += 1  # Move right
            y -= 1  # Move down

    return (x, y)

n = int(input())
x, y = hex_spiral_coordinates(n)
print(x, y)