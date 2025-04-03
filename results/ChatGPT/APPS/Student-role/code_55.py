def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any point in the visible area of the white sheet
    # The visible area of the white sheet is outside the boundaries of the black sheets.
    
    # Check if the white sheet is completely covered by the black sheets
    is_covered_by_first_black = (x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2)
    is_covered_by_second_black = (x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2)

    # If both black sheets cover the white sheet completely, return "NO"
    if is_covered_by_first_black and is_covered_by_second_black:
        return "NO"

    # Check visibility on the left side of the white sheet
    if (x3 >= x2 or x5 >= x2) or (y3 >= y2 or y5 >= y2):
        return "YES"

    # Check visibility on the right side of the white sheet
    if (x4 <= x1 or x6 <= x1) or (y4 <= y1 or y6 <= y1):
        return "YES"

    # Check visibility on the top side of the white sheet
    if (y3 >= y2 or y5 >= y2) or (x3 >= x2 or x5 >= x2):
        return "YES"

    # Check visibility on the bottom side of the white sheet
    if (y4 <= y1 or y6 <= y1) or (x4 <= x1 or x6 <= x1):
        return "YES"

    # If all checks fail, then the white sheet is completely covered
    return "NO"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output result
print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))