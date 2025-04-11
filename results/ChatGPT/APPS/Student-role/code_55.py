def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any part of the white sheet that is not covered by both black sheets
    # Check the four corners of the white sheet
    corners = [
        (x1, y1),  # bottom left
        (x1, y2),  # top left
        (x2, y1),  # bottom right
        (x2, y2)   # top right
    ]
    
    for x, y in corners:
        # Check if the point (x, y) is outside the white sheet
        if not (x1 < x < x2 and y1 < y < y2):
            # Check if the point (x, y) is outside both black sheets
            if not (x3 < x < x4 and y3 < y < y4) and not (x5 < x < x6 and y5 < y < y6):
                return "YES"
    
    return "NO"

# Input reading
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))