def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any part of the white sheet that is not covered by both black sheets
    # The white sheet is visible if any of the following conditions are true:
    
    # Check left side of the white sheet
    if x1 > x4 and x1 > x6:  # left of white is right of both black sheets
        return "YES"
    
    # Check right side of the white sheet
    if x2 < x3 and x2 < x5:  # right of white is left of both black sheets
        return "YES"
    
    # Check bottom side of the white sheet
    if y1 > y4 and y1 > y6:  # bottom of white is above both black sheets
        return "YES"
    
    # Check top side of the white sheet
    if y2 < y3 and y2 < y5:  # top of white is below both black sheets
        return "YES"
    
    return "NO"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))