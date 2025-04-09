def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for height in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % height == 0:
            width = total_tiles // height
            
            # Check if we can fit red and blue
            for w in range(1, width + 1):
                h_r = (a + w - 1) // w  # Minimum height for red
                h_b = (b + (width - w) - 1) // (width - w) if (width - w) > 0 else float('inf')

                if h_r + h_b <= height:
                    perimeter = 2 * (width + height)
                    min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

# Read input
a, b = map(int, input().split())
# Calculate and print the minimal perimeter
print(minimal_perimeter(a, b))