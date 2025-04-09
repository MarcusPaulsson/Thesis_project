def find_coordinates(n):
    if n == 0:
        return (0, 0)
    
    layer = 0
    moves_in_layer = 1
    
    # Find the layer where the n-th move is located
    while n >= moves_in_layer:
        n -= moves_in_layer
        layer += 1
        moves_in_layer = layer * 6
    
    # Calculate the coordinates
    x, y = layer, 0
    
    # Determine the direction of the n-th move in the current layer
    if n == 0:
        return (x, y)
    
    # Each layer is made of 6 segments
    # Each segment has layer length, except the last one which has n moves
    directions = [
        (1, 0),      # Right
        (0, 1),      # Top-right
        (-1, 1),     # Top-left
        (-1, 0),     # Left
        (0, -1),     # Bottom-left
        (1, -1)      # Bottom-right
    ]
    
    # Move through the segments
    for i in range(6):
        if n <= layer:
            dx, dy = directions[i]
            return (x + dx * n, y + dy * n)
        n -= layer
        x += directions[i][0] * layer
        y += directions[i][1] * layer
    
    return (x, y)

n = int(input())
x, y = find_coordinates(n)
print(x, y)