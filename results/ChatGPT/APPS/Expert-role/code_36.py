def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 1

    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    x, y = layer, 0

    if n == 0:
        return (x, y)

    # Move to the starting point of the next layer
    x -= 1
    n -= 1

    # Each segment of the layer has a length of `layer`
    # There are 6 segments in total
    segment_length = layer

    # Determine the segment and the position within the segment
    segment = n // segment_length
    position_in_segment = n % segment_length

    # Move based on the segment
    if segment == 0:  # Right
        x += position_in_segment
        y += 0
    elif segment == 1:  # Top-right
        x += segment_length
        y += position_in_segment
    elif segment == 2:  # Top-left
        x += segment_length - position_in_segment
        y += segment_length
    elif segment == 3:  # Left
        x -= position_in_segment
        y += segment_length - position_in_segment
    elif segment == 4:  # Bottom-left
        x -= segment_length
        y -= position_in_segment
    elif segment == 5:  # Bottom-right
        x -= segment_length - position_in_segment
        y -= segment_length

    return (x, y)

n = int(input())
x, y = hexagonal_coordinates(n)
print(x, y)