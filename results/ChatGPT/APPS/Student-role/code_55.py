def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is a visible part of the white sheet
    # by checking the corners of the white sheet
    # against the black sheets

    # Check if the white sheet is completely covered by both black sheets
    if (x3 >= x2 or x4 <= x1 or y3 >= y2 or y4 <= y1) and (x5 >= x2 or x6 <= x1 or y5 >= y2 or y6 <= y1):
        return "YES"

    # Check for each corner of the white sheet if it's visible
    # i.e., if it lies outside the black sheets
    corners = [
        (x1, y1), (x1, y2), (x2, y1), (x2, y2)
    ]

    for x, y in corners:
        if not (x3 < x < x4 and y3 < y < y4) and not (x5 < x < x6 and y5 < y < y6):
            return "YES"

    return "NO"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output result
print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))