def solve():
    n = int(input())

    if n == 0:
        print(0, 0)
        return

    layer = 0
    while True:
        moves_in_layer = 6 * layer
        if n <= moves_in_layer:
            break
        n -= moves_in_layer
        layer += 1

    side = (n - 1) // layer
    rem = (n - 1) % layer

    if side == 0:
        x = 2 * layer - rem
        y = 2 * rem
    elif side == 1:
        x = layer - 2 * rem
        y = 2 * layer
    elif side == 2:
        x = -layer - rem
        y = 2 * layer - 2 * rem
    elif side == 3:
        x = -2 * layer + rem
        y = -2 * rem
    elif side == 4:
        x = -layer + 2 * rem
        y = -2 * layer
    else:
        x = layer + rem
        y = -2 * layer + 2 * rem

    print(x, y)

solve()