def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 0

    while moves_in_layer <= n:
        layer += 1
        moves_in_layer = 3 * layer * (layer + 1)  # Total moves in the current layer

    layer -= 1
    moves_in_layer = 3 * layer * (layer + 1)  # Total moves in the previous layer
    remaining_moves = n - moves_in_layer

    x, y = layer, 0  # Start at the rightmost point of the current layer

    if remaining_moves == 0:
        return (x, y)

    # Move counter-clockwise around the hexagon
    if remaining_moves <= layer:
        x -= remaining_moves
    elif remaining_moves <= 2 * layer:
        x = -layer
        y = remaining_moves - layer
    else:
        x = remaining_moves - 3 * layer
        y = layer

    return (x, y)

n = int(input().strip())
x, y = hexagonal_coordinates(n)
print(x, y)