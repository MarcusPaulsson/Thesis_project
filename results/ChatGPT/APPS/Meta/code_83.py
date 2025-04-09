def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check for both orientations
            for w, h in [(width, height), (height, width)]:
                # Check if red can fit as a rectangle
                if (a % w == 0 and (a // w) <= h) or (a % h == 0 and (a // h) <= w):
                    # Check if blue can fit as a rectangle
                    if (b % w == 0 and (b // w) <= h) or (b % h == 0 and (b // h) <= w):
                        perimeter = 2 * (w + h)
                        min_perimeter = min(min_perimeter, perimeter)
    
    return min_perimeter

# Read input
a, b = map(int, input().split())
# Output the result
print(minimal_perimeter(a, b))