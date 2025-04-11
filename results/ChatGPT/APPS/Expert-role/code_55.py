def is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the white sheet is completely covered by the two black sheets
    covered_left = max(x3, x5)
    covered_right = min(x4, x6)
    covered_bottom = max(y3, y5)
    covered_top = min(y4, y6)

    # Check if the covered area is valid
    if covered_left < covered_right and covered_bottom < covered_top:
        # Check if the white sheet is completely covered
        if (x1 >= covered_left and x2 <= covered_right and
                y1 >= covered_bottom and y2 <= covered_top):
            return "NO"

    return "YES"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))