def hexagon_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 1

    # Determine the layer in which the move n is located
    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    # Calculate the coordinates based on the layer and remaining moves
    x, y = layer, 0
    if n > 0:
        # Move in the hexagonal pattern
        direction = n // layer
        steps = n % layer

        if direction == 0:  # Right
            x += steps
        elif direction == 1:  # Top-right
            x += steps
            y += steps
        elif direction == 2:  # Top-left
            x -= steps
            y += steps
        elif direction == 3:  # Left
            x -= steps
        elif direction == 4:  # Bottom-left
            x -= steps
            y -= steps
        elif direction == 5:  # Bottom-right
            x += steps
            y -= steps

    return (x, y)

n = int(input().strip())
x, y = hexagon_coordinates(n)
print(x, y)