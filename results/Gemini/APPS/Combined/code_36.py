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
    x, y = 2 * layer, 0

    segment_length = layer

    if remaining == 0:
        print(x, y)
        return

    if remaining <= segment_length:
        x -= remaining
        y += 2 * remaining
    elif remaining <= 2 * segment_length:
        remaining -= segment_length
        x -= 2 * segment_length
        y += 2 * segment_length
        x -= remaining
        y -= remaining
    elif remaining <= 3 * segment_length:
        remaining -= 2 * segment_length
        x -= 2 * segment_length
        y += 2 * segment_length
        x += remaining
        y -= remaining * 2
    elif remaining <= 4 * segment_length:
        remaining -= 3 * segment_length
        x += remaining
        y -= 2 * segment_length
    elif remaining <= 5 * segment_length:
        remaining -= 4 * segment_length
        x += 2 * segment_length
        y -= 2 * segment_length
        x += remaining
        y += 2 * remaining
    else:
        remaining -= 5 * segment_length
        x += 2 * segment_length
        y -= 2 * segment_length
        x -= remaining
        y += 2 * remaining

    print(x, y)

solve()