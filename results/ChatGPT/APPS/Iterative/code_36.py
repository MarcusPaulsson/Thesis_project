def hexagon_coordinates(n):
    if n == 0:
        return (0, 0)
    
    layer = 0
    moves_in_layer = 0
    
    # Finding which layer the n-th move falls into
    while moves_in_layer <= n:
        layer += 1
        moves_in_layer += 6 * layer
    
    # Adjusting layer and moves_in_layer to the last valid layer
    layer -= 1
    moves_in_layer -= 6 * layer
    
    # Calculate position within the identified layer
    position_in_layer = n - moves_in_layer
    x, y = layer, 0  # Starting point of the layer in the coordinate system
    
    if position_in_layer == 0:
        return (x, y)
    
    direction = position_in_layer // layer
    steps = position_in_layer % layer

    # Move according to the calculated direction and steps
    if direction == 0:  # Right
        x += steps
    elif direction == 1:  # Up-right
        x += layer
        y += steps
    elif direction == 2:  # Up-left
        x += layer - steps
        y += layer
    elif direction == 3:  # Left
        x -= steps
        y += layer
    elif direction == 4:  # Down-left
        x -= layer
        y -= steps
    elif direction == 5:  # Down-right
        x -= layer - steps
        y -= layer
    
    return (x, y)

n = int(input().strip())
x, y = hexagon_coordinates(n)
print(x, y)