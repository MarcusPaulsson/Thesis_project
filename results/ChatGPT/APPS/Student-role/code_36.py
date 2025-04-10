def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)
    
    layer = 0
    moves_in_layer = 6 * layer
    
    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = 6 * layer
    
    x, y = layer, 0
    
    if n == 0:
        return (x, y)
    
    # Calculate the position in the current layer
    direction = n // layer
    steps = n % layer
    
    if direction == 0:  # Right
        x += steps
        y += 0
    elif direction == 1:  # Top-right
        x += steps
        y += steps
    elif direction == 2:  # Top-left
        x += 0
        y += steps
    elif direction == 3:  # Left
        x -= steps
        y += 0
    elif direction == 4:  # Bottom-left
        x -= steps
        y -= steps
    elif direction == 5:  # Bottom-right
        x += 0
        y -= steps
    
    return (x, y)

n = int(input())
x, y = hexagonal_coordinates(n)
print(x, y)