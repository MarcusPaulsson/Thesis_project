def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            # Check both configurations (width, height) and (height, width)
            for w, h in [(width, height), (height, width)]:
                # Check if we can fit a red rectangle and a blue rectangle
                for red_width in range(1, w + 1):
                    if a % red_width == 0:
                        red_height = a // red_width
                        if red_height <= h:
                            min_perimeter = min(min_perimeter, 2 * (w + h))
                            break

                for blue_width in range(1, w + 1):
                    if b % blue_width == 0:
                        blue_height = b // blue_width
                        if blue_height <= h:
                            min_perimeter = min(min_perimeter, 2 * (w + h))
                            break

    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))