def minimal_perimeter(a, b):
    total = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total**0.5) + 1):
        if total % width == 0:
            length = total // width
            
            # Check for red rectangle
            for red_width in range(1, int(a**0.5) + 1):
                if a % red_width == 0:
                    red_length = a // red_width
                    if red_width <= width and red_length <= length:
                        # Check for blue rectangle
                        for blue_width in range(1, int(b**0.5) + 1):
                            if b % blue_width == 0:
                                blue_length = b // blue_width
                                if blue_width <= width and blue_length <= length:
                                    perimeter = 2 * (width + length)
                                    min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))