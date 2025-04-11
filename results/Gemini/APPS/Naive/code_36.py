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

    remaining = n - count
    layer += 1

    if remaining == 0:
        x = 2 * layer - 1
        y = layer
    elif remaining <= layer:
        x = 2 * layer - remaining
        y = layer + 2 * remaining
    elif remaining <= 2 * layer:
        x = layer - 2 * (remaining - layer)
        y = 3 * layer
    elif remaining <= 3 * layer:
        x = -layer - (remaining - 2 * layer)
        y = layer + 2 * (3 * layer - remaining)
    elif remaining <= 4 * layer:
        x = -2 * layer + (remaining - 3 * layer)
        y = -layer - 2 * (remaining - 3 * layer)
    elif remaining <= 5 * layer:
        x = -layer + 2 * (remaining - 4 * layer)
        y = -3 * layer
    else:
        x = layer + (remaining - 5 * layer)
        y = -layer - 2 * (6 * layer - remaining)

    print(x, y)

solve()