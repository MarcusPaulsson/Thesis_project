def minimal_perimeter(a, b):
    min_perimeter = float('inf')

    for height_r in range(1, int(a**0.5) + 1):
        if a % height_r == 0:
            width_r = a // height_r
            
            for height_b in range(1, int(b**0.5) + 1):
                if b % height_b == 0:
                    width_b = b // height_b
                    
                    # Calculate perimeter for both arrangements
                    perimeters = [
                        2 * (max(height_r, height_b) + (width_r + width_b)),
                        2 * ((height_r + height_b) + max(width_r, width_b))
                    ]
                    min_perimeter = min(min_perimeter, *perimeters)

    return min_perimeter

# Input reading
a, b = map(int, input().strip().split())
print(minimal_perimeter(a, b))