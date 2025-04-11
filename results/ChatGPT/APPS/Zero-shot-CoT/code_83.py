def minimal_perimeter(a, b):
    min_perimeter = float('inf')
    
    for width in range(1, int((a + b) ** 0.5) + 2):
        if (a + b) % width == 0:
            height = (a + b) // width
            
            # Check red rectangle
            for red_width in range(1, int(a ** 0.5) + 2):
                if a % red_width == 0:
                    red_height = a // red_width
                    red_perimeter = 2 * (red_width + red_height)
                    
                    # Check blue rectangle
                    for blue_width in range(1, int(b ** 0.5) + 2):
                        if b % blue_width == 0:
                            blue_height = b // blue_width
                            blue_perimeter = 2 * (blue_width + blue_height)
                            
                            # Check if they fit in the overall rectangle
                            if (red_width <= width and red_height <= height) or (red_height <= width and red_width <= height):
                                if (blue_width <= width and blue_height <= height) or (blue_height <= width and blue_width <= height):
                                    total_perimeter = 2 * (width + height)
                                    min_perimeter = min(min_perimeter, total_perimeter)
    
    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))