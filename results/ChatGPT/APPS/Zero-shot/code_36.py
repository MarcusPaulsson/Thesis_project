def hexagonal_spiral(n):
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

    direction = remaining_moves // 1
    if direction == 1:
        x, y = layer, 0
    elif direction == 2:
        x, y = layer - (remaining_moves - 1), remaining_moves - 1
    elif direction == 3:
        x, y = -remaining_moves + 1, layer
    elif direction == 4:
        x, y = -layer, layer - (remaining_moves - 3)
    elif direction == 5:
        x, y = -layer + (remaining_moves - 4), -layer
    elif direction == 6:
        x, y = remaining_moves - 5, -layer + (remaining_moves - 5)

    return (x, y)

n = int(input().strip())
result = hexagonal_spiral(n)
print(result[0], result[1])