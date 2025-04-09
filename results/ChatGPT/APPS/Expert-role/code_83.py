def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check for red rectangle
            for r_width in range(1, int(a**0.5) + 1):
                if a % r_width == 0:
                    r_height = a // r_width
                    if r_width <= width and r_height <= height:
                        perimeter = 2 * (width + height)
                        min_perimeter = min(min_perimeter, perimeter)
                
            # Check for blue rectangle
            for b_width in range(1, int(b**0.5) + 1):
                if b % b_width == 0:
                    b_height = b // b_width
                    if b_width <= width and b_height <= height:
                        perimeter = 2 * (width + height)
                        min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))