def minimal_perimeter(a, b):
    total = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total**0.5) + 1):
        if total % width == 0:
            height = total // width
            
            # Check all combinations of width and height for red and blue rectangles
            for (x, y) in [(width, height), (height, width)]:
                # Check for red rectangle
                for red_width in range(1, int(x**0.5) + 1):
                    if a % red_width == 0:
                        red_height = a // red_width
                        if red_height <= y:
                            # Check for blue rectangle
                            for blue_width in range(1, int(x**0.5) + 1):
                                if b % blue_width == 0:
                                    blue_height = b // blue_width
                                    if blue_height <= y:
                                        perimeter = 2 * (x + y)
                                        min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Read input
a, b = map(int, input().split())
# Print the result
print(minimal_perimeter(a, b))