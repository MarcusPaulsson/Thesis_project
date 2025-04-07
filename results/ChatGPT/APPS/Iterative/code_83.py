def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    # Check all possible dimensions for the total rectangle
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width

            # Check for all possible dimensions of the red rectangle
            for r_width in range(1, int(a**0.5) + 1):
                if a % r_width == 0:
                    r_height = a // r_width
                    # Ensure red rectangle fits within the total rectangle
                    if (r_width <= width and r_height <= height) or (r_height <= width and r_width <= height):
                        # Check for all possible dimensions of the blue rectangle
                        for b_width in range(1, int(b**0.5) + 1):
                            if b % b_width == 0:
                                b_height = b // b_width
                                # Ensure blue rectangle fits within the total rectangle
                                if (b_width <= width and b_height <= height) or (b_height <= width and b_width <= height):
                                    # Calculate perimeter
                                    perimeter = 2 * (width + height)
                                    min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Read input
a, b = map(int, input().split())
print(minimal_perimeter(a, b))