def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check if we can fit a rectangles for both colors
            for color_tiles in (a, b):
                for color_width in range(1, int(color_tiles**0.5) + 1):
                    if color_tiles % color_width == 0:
                        color_height = color_tiles // color_width
                        # Check the perimeter of the enclosing rectangle
                        perimeter = 2 * (width + height)
                        min_perimeter = min(min_perimeter, perimeter)

                        # Check the other orientation
                        perimeter = 2 * (color_height + color_width)
                        min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))