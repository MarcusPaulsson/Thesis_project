def get_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    while n >= 3 * layer * (layer + 1):
        layer += 1

    n -= 3 * (layer - 1) * layer  # Moves in the previous layers
    x, y = layer, 0

    # Calculate position based on remaining moves in the current layer
    if n < layer:
        x -= n
    elif n < 2 * layer:
        x -= layer
        y += n - layer
    else:
        x += n - 2 * layer
        y += layer

    return (x, y)

n = int(input())
x, y = get_coordinates(n)
print(x, y)