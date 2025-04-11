def solve():
    n = int(input())

    if n == 0:
        print(0, 0)
        return

    layer = 0
    count = 0
    while True:
        if count + 6 * layer <= n:
            count += 6 * layer
            layer += 1
        else:
            layer -= 1
            break

    remaining_moves = n - count
    x, y = 2 * layer, 0

    if remaining_moves == 0:
        print(x, y)
        return

    segment_length = layer
    
    if layer == 0:
        x = remaining_moves * 2
        y = 0
        print(x, y)
        return

    moves_in_segment = remaining_moves % (6 * layer)
    
    if 0 < remaining_moves <= layer:
        x -= 2 * remaining_moves
    elif layer < remaining_moves <= 2 * layer:
        x -= 2 * layer
        x += 2 * (remaining_moves - layer)
        y += 2 * layer
    elif 2 * layer < remaining_moves <= 3 * layer:
        x += 2 * (remaining_moves - 2 * layer)
        y += 2 * layer
        y -= 2 * (remaining_moves - 2 * layer)
    elif 3 * layer < remaining_moves <= 4 * layer:
        x += 2 * layer
        y -= 2 * (remaining_moves - 3 * layer)
    elif 4 * layer < remaining_moves <= 5 * layer:
        x += 2 * layer
        x -= 2 * (remaining_moves - 4 * layer)
        y -= 2 * layer
    else:
        x -= 2 * (remaining_moves - 5 * layer)
        y -= 2 * layer
        y += 2 * (remaining_moves - 5 * layer)

    print(x, y)

solve()