def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any part of the white sheet that is not covered by both black sheets
    # The white sheet is visible if there is at least one point that is:
    # - Not strictly inside the white sheet (i.e., outside or on the border)
    # - Strictly outside both black sheets

    # Check the left side of the white sheet
    if x1 > x3 and x1 > x5:
        return "YES"
    
    # Check the right side of the white sheet
    if x2 < x4 and x2 < x6:
        return "YES"
    
    # Check the bottom side of the white sheet
    if y1 > y4 and y1 > y6:
        return "YES"
    
    # Check the top side of the white sheet
    if y2 < y3 and y2 < y5:
        return "YES"
    
    # Check if the white sheet is completely covered by both black sheets
    if (x3 <= x1 < x4 and y3 <= y1 < y4 and
        x3 < x2 <= x4 and y3 < y2 <= y4) or \
       (x5 <= x1 < x6 and y5 <= y1 < y6 and
        x5 < x2 <= x6 and y5 < y2 <= y6):
        return "NO"
    
    # If none of the above conditions are met, the white sheet is visible
    return "YES"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))