def min_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            for (w, h) in [(width, height), (height, width)]:
                if (w * h == total_tiles):
                    # Check if we can form rectangles for red and blue
                    for red_width in range(1, int(a**0.5) + 1):
                        if a % red_width == 0:
                            red_height = a // red_width
                            if (red_width <= w and red_height <= h) or (red_height <= w and red_width <= h):
                                for blue_width in range(1, int(b**0.5) + 1):
                                    if b % blue_width == 0:
                                        blue_height = b // blue_width
                                        if (blue_width <= w and blue_height <= h) or (blue_height <= w and blue_width <= h):
                                            perimeter = 2 * (w + h)
                                            min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter

# Read input
a, b = map(int, input().split())
# Output the result
print(min_perimeter(a, b))