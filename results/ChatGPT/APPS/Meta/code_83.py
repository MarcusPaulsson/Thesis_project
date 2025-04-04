def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    # Iterate over all possible dimensions of the rectangle
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Check possible red rectangle dimensions
                for red_width in range(1, w + 1):
                    if a % red_width == 0:
                        red_height = a // red_width
                        if red_height <= h:
                            perimeter = 2 * (w + h)
                            min_perimeter = min(min_perimeter, perimeter)
                
                # Check possible blue rectangle dimensions
                for blue_width in range(1, w + 1):
                    if b % blue_width == 0:
                        blue_height = b // blue_width
                        if blue_height <= h:
                            perimeter = 2 * (w + h)
                            min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Input
a, b = map(int, input().split())
# Output
print(minimal_perimeter(a, b))