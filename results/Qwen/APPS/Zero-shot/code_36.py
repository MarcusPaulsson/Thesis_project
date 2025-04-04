def find_location(n):
    if n == 0:
        return 0, 0

    layer = (n - 1) // 6
    offset = (n - 1) % 6

    if offset == 0:
        return layer, -layer
    elif offset == 1:
        return layer + 1, -layer
    elif offset == 2:
        return layer + 1, layer
    elif offset == 3:
        return layer, layer + 1
    elif offset == 4:
        return -layer, layer + 1
    elif offset == 5:
        return -layer - 1, layer

n = int(input())
x, y = find_location(n)
print(x, y)