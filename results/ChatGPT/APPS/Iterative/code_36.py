def hexagonal_spiral(n):
    if n == 0:
        return (0, 0)

    layer = 0
    while n > 3 * layer * (layer + 1):
        layer += 1
    
    moves_in_previous_layer = 3 * layer * (layer - 1)
    position_in_layer = n - moves_in_previous_layer

    if position_in_layer < layer:
        x = layer
        y = position_in_layer - layer
    elif position_in_layer < 2 * layer:
        x = layer - (position_in_layer - layer)
        y = layer
    else:
        x = -layer
        y = layer - (position_in_layer - 2 * layer)

    return (x, y)

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer: ").strip())
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        x, y = hexagonal_spiral(n)
        print(x, y)
    except ValueError as e:
        print(e)