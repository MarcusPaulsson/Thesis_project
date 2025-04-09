def can_see_white_sheet(white_coords, black1_coords, black2_coords):
    x1, y1, x2, y2 = white_coords
    x3, y3, x4, y4 = black1_coords
    x5, y5, x6, y6 = black2_coords

    # Check visibility conditions
    left_visible = (x3 >= x2 or x4 >= x2) or (x5 >= x2 or x6 >= x2)
    right_visible = (x3 <= x1 or x4 <= x1) or (x5 <= x1 or x6 <= x1)
    bottom_visible = (y3 >= y2 or y4 >= y2) or (y5 >= y2 or y6 >= y2)
    top_visible = (y3 <= y1 or y4 <= y1) or (y5 <= y1 or y6 <= y1)

    if left_visible or right_visible or bottom_visible or top_visible:
        return "YES"

    # Check if the black sheets completely cover the white sheet
    fully_covered = (
        (x3 <= x1 and x4 >= x2 and y3 <= y1 and y4 >= y2) or
        (x5 <= x1 and x6 >= x2 and y5 <= y1 and y6 >= y2) or
        (x3 <= x1 and x4 >= x2 and y5 <= y1 and y6 >= y2) or
        (x5 <= x1 and x6 >= x2 and y3 <= y1 and y4 >= y2)
    )

    return "NO" if fully_covered else "YES"

# Read input values
white_coords = list(map(int, input().split()))
black1_coords = list(map(int, input().split()))
black2_coords = list(map(int, input().split()))

# Get the result and print it
result = can_see_white_sheet(white_coords, black1_coords, black2_coords)
print(result)