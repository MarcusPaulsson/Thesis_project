def is_visible_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the black sheets cover the entire area of the white sheet
    covered_left = max(x3, x5)  # farthest left covered by black sheets
    covered_right = min(x4, x6)  # farthest right covered by black sheets
    covered_bottom = max(y3, y5)  # highest bottom covered by black sheets
    covered_top = min(y4, y6)  # lowest top covered by black sheets
    
    # Check if the white sheet is completely covered
    if covered_left < x2 and covered_right > x1 and covered_bottom < y2 and covered_top > y1:
        return "NO"
    else:
        return "YES"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output result
print(is_visible_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))