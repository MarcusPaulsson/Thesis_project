def get_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    moves_in_layer = 6
    total_moves = 0
    
    while total_moves + moves_in_layer <= n:
        total_moves += moves_in_layer
        layer += 1
        moves_in_layer += 6

    remaining_moves = n - total_moves
    x, y = layer, 0

    if remaining_moves == 0:
        return (x, y)

    # Move in the current layer
    direction = 0  # Start moving right (east)
    for _ in range(remaining_moves):
        if direction == 0:  # East
            x += 1
        elif direction == 1:  # North-East
            y += 1
            x -= 1
        elif direction == 2:  # North-West
            y += 1
        elif direction == 3:  # West
            x -= 1
        elif direction == 4:  # South-West
            y -= 1
            x += 1
        elif direction == 5:  # South-East
            y -= 1
        
        direction = (direction + 1) % 6

    return (x, y)

n = int(input())
x, y = get_coordinates(n)
print(x, y)