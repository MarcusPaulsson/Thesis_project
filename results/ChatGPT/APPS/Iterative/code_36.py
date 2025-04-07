def hexagonal_spiral(n):
    if n == 0:
        return (0, 0)
    
    layer = 0
    while n > 6 * layer:
        n -= 6 * layer
        layer += 1
    
    x, y = layer, 0
    
    if n == 0:
        return (x, y)
    
    # Determine the position in the current layer
    segment_length = layer
    if n <= segment_length:
        x -= n
        y += 0
    elif n <= 2 * segment_length:
        x -= segment_length
        y += n - segment_length
    elif n <= 3 * segment_length:
        x += n - 2 * segment_length
        y += segment_length
    elif n <= 4 * segment_length:
        x += segment_length
        y -= n - 3 * segment_length
    elif n <= 5 * segment_length:
        x += n - 4 * segment_length
        y -= segment_length
    else:
        x -= segment_length
        y -= n - 5 * segment_length
    
    return (x, y)

n = int(input())
x, y = hexagonal_spiral(n)
print(x, y)