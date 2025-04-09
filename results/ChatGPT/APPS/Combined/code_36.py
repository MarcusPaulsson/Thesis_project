def hexagon_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine the layer of the hexagonal spiral
    layer = 0
    moves_in_layer = 1

    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    # Calculate the position in the current layer
    x, y = layer, 0

    if n == 0:
        return (x, y)

    # Each segment has 'layer' moves
    segment = n // layer
    position_in_segment = n % layer

    # Move to the corresponding direction based on segment
    if segment == 0:  # First segment
        x += position_in_segment
    elif segment == 1:  # Second segment
        x -= position_in_segment
        y += position_in_segment
    elif segment == 2:  # Third segment
        x -= position_in_segment
        y -= position_in_segment
    elif segment == 3:  # Fourth segment
        x -= position_in_segment
        y += position_in_segment
    elif segment == 4:  # Fifth segment
        x += position_in_segment
        y -= position_in_segment
    elif segment == 5:  # Sixth segment
        x += position_in_segment

    return (x, y)

# Read input
n = int(input().strip())
# Get coordinates
result = hexagon_coordinates(n)
# Print result
print(result[0], result[1])