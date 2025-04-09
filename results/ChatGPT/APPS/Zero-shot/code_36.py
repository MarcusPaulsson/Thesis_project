def hexagonal_coordinates(n):
    if n == 0:
        return (0, 0)

    layer = 0
    steps_in_layer = 6
    moves = 0
    
    while moves + steps_in_layer <= n:
        moves += steps_in_layer
        layer += 1
        steps_in_layer += 6

    remaining_moves = n - moves
    x, y = layer, 0

    if remaining_moves == 0:
        return (x, y)

    # Directions for hexagonal grid: right, top-right, top-left, left, bottom-left, bottom-right
    directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    
    # Apply the remaining moves in the current layer
    for i in range(remaining_moves):
        dx, dy = directions[i % 6]
        x += dx
        y += dy

    return (x, y)

n = int(input().strip())
result = hexagonal_coordinates(n)
print(result[0], result[1])