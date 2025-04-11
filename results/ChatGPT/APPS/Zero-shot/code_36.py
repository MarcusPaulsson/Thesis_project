def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)
    
    layer = 0
    moves_in_layer = 6 * layer
    
    while n > moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer
    
    # The coordinates for the starting point of the layer
    x, y = layer, 0
    
    # The number of steps to move in the current layer
    steps = n
    
    # Determine the direction and move accordingly
    for direction in range(6):
        if steps <= direction + 1:
            if direction == 0:
                x += steps
                break
            elif direction == 1:
                x -= 1
                y += steps
                break
            elif direction == 2:
                x -= 1
                y -= steps
                break
            elif direction == 3:
                x += steps
                y -= 1
                break
            elif direction == 4:
                x += 1
                y -= steps
                break
            elif direction == 5:
                x += 1
                y += steps
                break
        steps -= direction + 1
    
    return (x, y)

n = int(input().strip())
x, y = hexagonal_coordinates(n)
print(x, y)