def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    # Iterate through possible widths of the rectangle
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Check if we can fit a red rectangle and a blue rectangle
                if (a % w == 0 and a // w <= h) or (b % w == 0 and b // w <= h):
                    perimeter = 2 * (w + h)
                    min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Input reading
a, b = map(int, input().split())
print(minimal_perimeter(a, b))