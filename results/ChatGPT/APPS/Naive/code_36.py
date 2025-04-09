def hex_spiral_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine the layer of the spiral
    layer = 0
    while n > 6 * layer * (layer + 1) // 2:
        layer += 1

    # Calculate the position in the current layer
    position_in_layer = n - 6 * (layer - 1) * layer // 2
    side_length = layer

    # Calculate hexagon coordinates based on the layer and position
    x, y = 0, 0
    if position_in_layer <= side_length:
        x = side_length
        y = position_in_layer - side_length
    elif position_in_layer <= 2 * side_length:
        x = side_length - (position_in_layer - side_length)
        y = side_length
    elif position_in_layer <= 3 * side_length:
        x = -side_length
        y = side_length - (position_in_layer - 2 * side_length)
    elif position_in_layer <= 4 * side_length:
        x = -side_length + (position_in_layer - 3 * side_length)
        y = -side_length
    elif position_in_layer <= 5 * side_length:
        x = side_length
        y = -side_length + (position_in_layer - 4 * side_length)
    else:
        x = side_length - (position_in_layer - 5 * side_length)
        y = side_length

    return (x, y)

n = int(input())
x, y = hex_spiral_coordinates(n)
print(x, y)