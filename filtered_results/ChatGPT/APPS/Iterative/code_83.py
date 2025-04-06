def min_perimeter(a, b):
    total_tiles = a + b
    min_perim = float('inf')

    # Iterate through all possible width values for the rectangle containing a+b tiles
    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width

            # Check combinations of width and height for red tiles
            for r_width in range(1, int(a**0.5) + 1):
                if a % r_width == 0:
                    r_height = a // r_width
                    if r_width <= width and r_height <= height:
                        remaining_space = (width - r_width) * height + (height - r_height) * width
                        if b <= remaining_space:
                            min_perim = min(min_perim, 2 * (width + height))

            # Check combinations of width and height for blue tiles
            for b_width in range(1, int(b**0.5) + 1):
                if b % b_width == 0:
                    b_height = b // b_width
                    if b_width <= width and b_height <= height:
                        remaining_space = (width - b_width) * height + (height - b_height) * width
                        if a <= remaining_space:
                            min_perim = min(min_perim, 2 * (width + height))

    return min_perim if min_perim != float('inf') else 0

# Read input
a, b = map(int, input().split())
# Calculate and print the minimal perimeter
print(min_perimeter(a, b))