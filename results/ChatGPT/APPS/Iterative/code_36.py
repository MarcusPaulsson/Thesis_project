def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)
    
    layer = 0
    moves_in_layer = 0
    
    # Find the layer where the nth move is located
    while n > moves_in_layer + 6 * layer:
        moves_in_layer += 6 * layer
        layer += 1
    
    # Calculate the position in the current layer
    x, y = layer, 0
    position_in_layer = n - moves_in_layer
    
    # Determine the coordinates based on the position in the layer
    if position_in_layer < layer:
        x -= position_in_layer
    elif position_in_layer < 2 * layer:
        x -= layer
        y += position_in_layer - layer
    elif position_in_layer < 3 * layer:
        y += layer
        x += position_in_layer - 2 * layer
    elif position_in_layer < 4 * layer:
        x += layer
        y -= position_in_layer - 3 * layer
    elif position_in_layer < 5 * layer:
        y -= layer
        x -= position_in_layer - 4 * layer
    else:
        x -= position_in_layer - 5 * layer
    
    return (x, y)

n = int(input())
x, y = hexagonal_coordinates(n)
print(x, y)