def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Calculate the perimeter for the current rectangle configuration
            perimeter = 2 * (width + height)
            min_perimeter = min(min_perimeter, perimeter)

            # No need to check for swapped width and height as it gives the same perimeter
            
            # Check if we can form rectangles with the individual colors
            for color_tiles in (a, b):
                for color_width in range(1, int(color_tiles**0.5) + 1):
                    if color_tiles % color_width == 0:
                        color_height = color_tiles // color_width
                        perimeter = 2 * (color_width + color_height)
                        min_perimeter = min(min_perimeter, perimeter + 2 * (width + height))

    return min_perimeter

# Read input
a, b = map(int, input().strip().split())
# Output the result
print(minimal_perimeter(a, b))