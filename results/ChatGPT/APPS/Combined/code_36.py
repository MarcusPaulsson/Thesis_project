def find_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 0

    # Determine the layer in which the move n is located
    while n > moves_in_layer:
        layer += 1
        moves_in_layer = 6 * layer

    # Calculate the coordinates based on the layer and remaining moves
    x, y = layer, 0
    remaining_moves = n - (moves_in_layer - 6 * layer)

    if remaining_moves > 0:
        # Each segment of the layer corresponds to a direction
        direction = remaining_moves // layer
        steps = remaining_moves % layer

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
x, y = find_coordinates(n)
print(x, y)