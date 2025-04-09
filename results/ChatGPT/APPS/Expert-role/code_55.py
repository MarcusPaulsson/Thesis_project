def is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if any part of the white sheet is visible
    # The white sheet is visible if there is any point that:
    # 1. Is not strictly inside the white sheet (i.e., at least one of its edges)
    # 2. Is strictly outside both black sheets
    
    # Check bottom edge of the white sheet
    if y1 > y4 and y1 > y6:  # bottom edge of white is above both black sheets
        return "YES"
    
    # Check top edge of the white sheet
    if y2 < y3 and y2 < y5:  # top edge of white is below both black sheets
        return "YES"
    
    # Check left edge of the white sheet
    if x1 > x4 and x1 > x6:  # left edge of white is right of both black sheets
        return "YES"
    
    # Check right edge of the white sheet
    if x2 < x3 and x2 < x5:  # right edge of white is left of both black sheets
        return "YES"
    
    return "NO"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output result
print(is_white_sheet_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))