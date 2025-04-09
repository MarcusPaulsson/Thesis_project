def minimal_perimeter(a, b):
    min_perimeter = float('inf')
    
    # Iterate through all possible widths of the rectangle
    for width in range(1, int((a + b) ** 0.5) + 2):
        if (a + b) % width == 0:
            height = (a + b) // width
            
            # Check both orientations
            for w, h in [(width, height), (height, width)]:
                # Check if we can fit red and blue rectangles
                if (a % w == 0 and a // w <= h) or (b % w == 0 and b // w <= h):
                    perimeter = 2 * (w + h)
                    min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))