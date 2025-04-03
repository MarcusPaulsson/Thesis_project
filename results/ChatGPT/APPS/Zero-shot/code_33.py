def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Check red rectangle
                if a % w == 0:
                    red_height = a // w
                    if red_height <= h:
                        # Check blue rectangle
                        if b % (h - red_height) == 0:
                            blue_width = b // (h - red_height)
                            if blue_width <= w:
                                perimeter = 2 * (w + h)
                                min_perimeter = min(min_perimeter, perimeter)

                # Check blue rectangle first
                if b % w == 0:
                    blue_height = b // w
                    if blue_height <= h:
                        # Check red rectangle
                        if a % (h - blue_height) == 0:
                            red_width = a // (h - blue_height)
                            if red_width <= w:
                                perimeter = 2 * (w + h)
                                min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Read input
a, b = map(int, input().split())
print(minimal_perimeter(a, b))