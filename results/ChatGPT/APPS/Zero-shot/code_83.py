def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Check if we can fit a red rectangle and a blue rectangle
                for r_width in range(1, w + 1):
                    if a % r_width == 0:
                        r_height = a // r_width
                        if r_height <= h:
                            min_perimeter = min(min_perimeter, 2 * (w + h))
                            break  # No need to check further for this width

                for b_width in range(1, w + 1):
                    if b % b_width == 0:
                        b_height = b // b_width
                        if b_height <= h:
                            min_perimeter = min(min_perimeter, 2 * (w + h))
                            break  # No need to check further for this width

    return min_perimeter

# Input reading
a, b = map(int, input().split())
print(minimal_perimeter(a, b))