def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')
    
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Ensure we can fit a red rectangle and a blue rectangle
                for r_width in range(1, w + 1):
                    if a % r_width == 0:
                        r_height = a // r_width
                        if r_height <= h:
                            # Now we have a valid red rectangle
                            # Calculate remaining area for blue
                            remaining_width = w
                            remaining_height = h - r_height
                            if remaining_height > 0 and remaining_width > 0:
                                for b_width in range(1, remaining_width + 1):
                                    if b % b_width == 0:
                                        b_height = b // b_width
                                        if b_height <= remaining_height:
                                            perimeter = 2 * (w + h)
                                            min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Input reading
a, b = map(int, input().split())
result = minimal_perimeter(a, b)
print(result)