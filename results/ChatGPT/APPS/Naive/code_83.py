def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            length = total_tiles // width
            
            for red_width in range(1, int(a**0.5) + 1):
                if a % red_width == 0:
                    red_length = a // red_width
                    if red_width <= width and red_length <= length:
                        # Check blue tiles can fit in remaining space
                        if (width - red_width) * length >= b:
                            min_perimeter = min(min_perimeter, 2 * (width + length))
                            
            for blue_width in range(1, int(b**0.5) + 1):
                if b % blue_width == 0:
                    blue_length = b // blue_width
                    if blue_width <= width and blue_length <= length:
                        # Check red tiles can fit in remaining space
                        if (width - blue_width) * length >= a:
                            min_perimeter = min(min_perimeter, 2 * (width + length))

    return min_perimeter

# Read input
a, b = map(int, input().strip().split())
# Output the result
print(minimal_perimeter(a, b))