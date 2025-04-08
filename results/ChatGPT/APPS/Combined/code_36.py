def get_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 1

    # Determine the layer of the hexagonal spiral
    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer

    # Calculate the initial position and determine the direction and steps in the current layer
    x, y = layer, 0
    direction = n // layer
    steps_in_direction = n % layer

    # Move based on the calculated direction
    if direction == 0:  # right
        x += steps_in_direction
    elif direction == 1:  # top-right
        x += layer
        y += steps_in_direction
    elif direction == 2:  # top-left
        x += layer - steps_in_direction
        y += layer
    elif direction == 3:  # left
        x -= steps_in_direction
        y += layer
    elif direction == 4:  # bottom-left
        x -= layer
        y -= steps_in_direction
    elif direction == 5:  # bottom-right
        x -= layer - steps_in_direction
        y -= layer

    return (x, y)

if __name__ == "__main__":
    n = int(input().strip())
    result = get_coordinates(n)
    print(result[0], result[1])