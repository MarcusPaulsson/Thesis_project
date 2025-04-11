def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    # Iterate through possible widths for the rectangle
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Check for red tiles
                for red_w in range(1, w + 1):
                    if a % red_w == 0:
                        red_h = a // red_w
                        if red_h <= h:
                            min_perimeter = min(min_perimeter, 2 * (w + h))
                
                # Check for blue tiles
                for blue_w in range(1, w + 1):
                    if b % blue_w == 0:
                        blue_h = b // blue_w
                        if blue_h <= h:
                            min_perimeter = min(min_perimeter, 2 * (w + h))

    return min_perimeter

# Read input
a, b = map(int, input().split())
# Print the result
print(minimal_perimeter(a, b))