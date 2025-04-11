def can_see_white_sheet(white_sheet, black_sheet1, black_sheet2):
    x1, y1, x2, y2 = white_sheet
    x3, y3, x4, y4 = black_sheet1
    x5, y5, x6, y6 = black_sheet2

    # Check if the white sheet is completely covered by both black sheets
    is_covered = (
        (x3 <= x1 < x4 and y3 <= y1 < y4) and
        (x5 <= x1 < x6 and y5 <= y1 < y6) and
        (x3 <= x2 <= x4 and y3 <= y2 <= y4) and
        (x5 <= x2 <= x6 and y5 <= y2 <= y6)
    )

    if is_covered:
        return "NO"

    # Check for visibility
    visible_left = x3 >= x2 or x5 >= x2
    visible_right = x4 <= x1 or x6 <= x1
    visible_below = y3 >= y2 or y5 >= y2
    visible_above = y4 <= y1 or y6 <= y1

    if visible_left or visible_right or visible_below or visible_above:
        return "YES"

    return "NO"

# Input reading
white_sheet = tuple(map(int, input().split()))
black_sheet1 = tuple(map(int, input().split()))
black_sheet2 = tuple(map(int, input().split()))

# Call the function and print the result
result = can_see_white_sheet(white_sheet, black_sheet1, black_sheet2)
print(result)