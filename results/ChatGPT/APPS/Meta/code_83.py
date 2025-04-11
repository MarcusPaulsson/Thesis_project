def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both orientations
            for w, h in [(width, height), (height, width)]:
                # Calculate perimeter
                perimeter = 2 * (w + h)
                
                # Check if we can fit red and blue rectangles
                if (a <= w * h) and (b <= w * h):
                    # Check if we can form rectangles for both colors
                    for red_width in range(1, w + 1):
                        if a % red_width == 0:
                            red_height = a // red_width
                            if red_height <= h:
                                min_perimeter = min(min_perimeter, perimeter)
                                break
                    for blue_width in range(1, w + 1):
                        if b % blue_width == 0:
                            blue_height = b // blue_width
                            if blue_height <= h:
                                min_perimeter = min(min_perimeter, perimeter)
                                break

    return min_perimeter

# Read input
a, b = map(int, input().split())
print(minimal_perimeter(a, b))