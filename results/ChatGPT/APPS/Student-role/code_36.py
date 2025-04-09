def get_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine which layer of the spiral the move is in
    layer = 0
    while n > 6 * layer:
        n -= 6 * layer
        layer += 1

    # Calculate the coordinates based on the layer and position within the layer
    x, y = layer, 0  # Start at the rightmost point of the current layer

    if n == 0:
        return (x, y)

    # Move counter-clockwise through the layer
    for direction in range(6):
        if n <= layer:
            if direction == 0:
                x -= n
            elif direction == 1:
                x -= layer
                y += n
            elif direction == 2:
                x -= layer
                y += layer
            elif direction == 3:
                x += n
                y += layer
            elif direction == 4:
                x += layer
                y -= n
            elif direction == 5:
                x += layer
                y -= layer
            break
        n -= layer

    return (x, y)

# Read input
n = int(input())
# Get coordinates
result = get_coordinates(n)
# Print output
print(result[0], result[1])