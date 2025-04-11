def get_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine the layer of the spiral
    layer = 0
    while n > 6 * layer:
        n -= 6 * layer
        layer += 1

    # Initialize coordinates based on the layer
    x, y = layer, 0

    # Calculate the coordinates based on the position in the layer
    if n > 0:
        if n <= layer:
            x -= n
        elif n <= 2 * layer:
            x = -layer
            y += (n - layer)
        elif n <= 3 * layer:
            x += (n - 2 * layer)
            y = layer
        elif n <= 4 * layer:
            x += layer
            y -= (n - 3 * layer)
        elif n <= 5 * layer:
            x = (n - 4 * layer) - layer
            y -= layer
        else:  # n <= 6 * layer
            x -= (layer - (n - 5 * layer))
            y = -layer

    return (x, y)

# Read input
n = int(input().strip())
# Get coordinates and print
coordinates = get_coordinates(n)
print(coordinates[0], coordinates[1])