def is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the white sheet is fully covered by both black sheets
    covered_left = max(x1, x3, x5)
    covered_right = min(x2, x4, x6)
    covered_bottom = max(y1, y3, y5)
    covered_top = min(y2, y4, y6)
    
    # Check if there is a visible area left
    if covered_left < covered_right and covered_bottom < covered_top:
        return "NO"
    else:
        return "YES"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output result
print(is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))