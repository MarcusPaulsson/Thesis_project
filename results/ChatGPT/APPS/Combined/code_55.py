def can_see_white_sheet(white, black1, black2):
    x1, y1, x2, y2 = white
    x3, y3, x4, y4 = black1
    x5, y5, x6, y6 = black2

    # Check if any part of the white sheet is visible
    visible = (
        x1 > x4 or  # Left of black sheet 1
        x2 < x3 or  # Right of black sheet 1
        y1 > y4 or  # Below black sheet 1
        y2 < y3 or  # Above black sheet 1
        x1 > x6 or  # Left of black sheet 2
        x2 < x5 or  # Right of black sheet 2
        y1 > y6 or  # Below black sheet 2
        y2 < y5     # Above black sheet 2
    )

    # Check if the white sheet is completely covered by both black sheets
    covered_by_black1 = (x3 < x1 < x4 and y3 < y1 < y4 and x3 < x2 < x4 and y3 < y2 < y4)
    covered_by_black2 = (x5 < x1 < x6 and y5 < y1 < y6 and x5 < x2 < x6 and y5 < y2 < y6)

    return visible or not (covered_by_black1 and covered_by_black2)

# Read input
white_sheet = tuple(map(int, input().split()))
black_sheet1 = tuple(map(int, input().split()))
black_sheet2 = tuple(map(int, input().split()))

# Determine if some part of the white sheet can be seen
if can_see_white_sheet(white_sheet, black_sheet1, black_sheet2):
    print("YES")
else:
    print("NO")