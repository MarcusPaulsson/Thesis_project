def get_coordinates(n):
    if n == 0:
        return (0, 0)

    # Determine the layer in which the move occurs
    layer = 0
    moves_in_layer = 1  # Starting with 1 move in layer 0
    total_moves = 1  # Total moves till current layer

    while total_moves <= n:
        layer += 1
        moves_in_layer = 6 * layer  # Each layer has 6 * layer moves
        total_moves += moves_in_layer

    # Total moves till the previous layer
    total_moves -= moves_in_layer
    remaining_moves = n - total_moves

    # Calculate the coordinates based on the layer and remaining moves
    x, y = layer, 0  # Start at the beginning of the layer

    # Move in the current layer
    for i in range(remaining_moves):
        if i < layer:
            x -= 1  # Move left
        elif i < 2 * layer:
            x -= 1  # Move left-down
            y += 1  # Move up
        elif i < 3 * layer:
            y += 1  # Move up
        elif i < 4 * layer:
            x += 1  # Move right-up
            y += 1  # Move up
        elif i < 5 * layer:
            x += 1  # Move right
        else:
            x += 1  # Move right-down
            y -= 1  # Move down

    return (x, y)

# Read input
n = int(input())
# Get coordinates
x, y = get_coordinates(n)
# Print result
print(x, y)