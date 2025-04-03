def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check for red rectangle with width and height
            if a <= width * height:
                red_width = min(width, a)
                red_height = (a + red_width - 1) // red_width
                if red_height <= height:
                    perimeter = 2 * (width + height)
                    min_perimeter = min(min_perimeter, perimeter)
                    
            # Check for blue rectangle with width and height
            if b <= width * height:
                blue_width = min(width, b)
                blue_height = (b + blue_width - 1) // blue_width
                if blue_height <= height:
                    perimeter = 2 * (width + height)
                    min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter

# Input
a, b = map(int, input().strip().split())
# Output
print(minimal_perimeter(a, b))