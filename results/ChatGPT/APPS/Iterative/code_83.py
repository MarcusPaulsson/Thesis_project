def minimal_perimeter(a, b):
    total_tiles = a + b
    min_perimeter = float('inf')

    for width in range(1, int(total_tiles**0.5) + 1):
        if total_tiles % width == 0:
            height = total_tiles // width
            
            for w, h in [(width, height), (height, width)]:
                if (a <= w * h and (a % w == 0 and a // w <= h)) or (b <= w * h and (b % w == 0 and b // w <= h)):
                    perimeter = 2 * (w + h)
                    min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter

a, b = map(int, input().split())
print(minimal_perimeter(a, b))