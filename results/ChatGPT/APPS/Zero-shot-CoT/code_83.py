def minimal_perimeter(a, b):
    min_perimeter = float('inf')
    
    # Iterate over all possible widths for the red rectangle
    for width_r in range(1, int(a**0.5) + 1):
        if a % width_r == 0:
            height_r = a // width_r
            
            # Now iterate over all possible widths for the blue rectangle
            for width_b in range(1, int(b**0.5) + 1):
                if b % width_b == 0:
                    height_b = b // width_b
                    
                    # Calculate the total width and height of the combined rectangle
                    total_width = max(width_r, width_b)
                    total_height = height_r + height_b
                    
                    # Calculate the perimeter
                    perimeter = 2 * (total_width + total_height)
                    min_perimeter = min(min_perimeter, perimeter)
                    
                    # Also check the other orientation for blue rectangle
                    total_width = width_r + width_b
                    total_height = max(height_r, height_b)
                    
                    perimeter = 2 * (total_width + total_height)
                    min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter

# Input reading
a, b = map(int, input().split())
print(minimal_perimeter(a, b))