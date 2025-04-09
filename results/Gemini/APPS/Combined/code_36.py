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

    # Segment 1
    if remaining <= segment_length:
        x -= 2 * remaining
        print(x, y)
        return
    else:
        x -= 2 * segment_length
        remaining -= segment_length

    # Segment 2
    y += 2 * remaining
    if remaining <= segment_length:
        print(x, y)
        return
    else:
        y += 2 * segment_length
        remaining -= segment_length

    # Segment 3
    x += 2 * remaining
    if remaining <= segment_length:
        print(x, y)
        return
    else:
        x += 2 * segment_length
        remaining -= segment_length

    # Segment 4
    y -= 2 * remaining
    if remaining <= segment_length:
        print(x, y)
        return
    else:
        y -= 2 * segment_length
        remaining -= segment_length

    # Segment 5
    x -= 2 * remaining
    if remaining <= segment_length:
        print(x, y)
        return
    else:
        x -= 2 * segment_length
        remaining -= segment_length
    
    # Segment 6
    y += 2 * remaining
    print(x, y)

solve()