def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 1

    # Determine the layer where the nth move is located
    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    # Starting coordinates at the beginning of the layer
    x, y = layer, 0

    # If no moves are left, return the current coordinates
    if n == 0:
        return (x, y)

    # Directions for moving in the hexagonal grid
    directions = [
        (1, 0),  # right
        (0, 1),  # top-right
        (-1, 1), # top-left
        (-1, 0), # left
        (0, -1), # bottom-left
        (1, -1)  # bottom-right
    ]

    # Move in the determined direction for the remaining moves
    for i in range(n):
        dx, dy = directions[i % 6]
        x += dx
        y += dy

    return (x, y)

n = int(input().strip())
x, y = hexagonal_coordinates(n)
print(x, y)