def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 6 * layer

    while n > moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    x, y = layer, 0
    direction = n // layer
    steps = n % layer

    if direction == 0:
        x -= steps
    elif direction == 1:
        x -= steps
        y += steps
    elif direction == 2:
        y += steps
    elif direction == 3:
        x += steps
    elif direction == 4:
        x += steps
        y -= steps
    elif direction == 5:
        y -= steps

    return (x, y)

n = int(input().strip())
x, y = hexagonal_coordinates(n)
print(x, y)