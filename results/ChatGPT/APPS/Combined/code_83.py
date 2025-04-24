def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check for red rectangle
            for red_width in range(1, int(a**0.5) + 1):
                if a % red_width == 0:
                    red_height = a // red_width
                    if red_width <= width and red_height <= height:
                        # Check for blue rectangle
                        for blue_width in range(1, int(b**0.5) + 1):
                            if b % blue_width == 0:
                                blue_height = b // blue_width
                                if blue_width <= width and blue_height <= height:
                                    perimeter = 2 * (width + height)
                                    min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Input reading
a, b = map(int, input().split())
print(minimal_perimeter(a, b))