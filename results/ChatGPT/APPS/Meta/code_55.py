def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the white sheet is completely covered by both black sheets
    covered_left = max(x3, x5)  # rightmost left edge of both black sheets
    covered_right = min(x4, x6)  # leftmost right edge of both black sheets
    covered_bottom = max(y3, y5)  # uppermost bottom edge of both black sheets
    covered_top = min(y4, y6)  # lowermost top edge of both black sheets

    # Check if the white sheet is fully covered
    if covered_left < covered_right and covered_bottom < covered_top:
        # If the black sheets cover the entirety of the white sheet
        if covered_left < x2 and covered_right > x1 and covered_bottom < y2 and covered_top > y1:
            return "NO"

    return "YES"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))