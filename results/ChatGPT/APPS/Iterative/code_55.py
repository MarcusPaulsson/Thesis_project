def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any part of the white sheet that is not covered by both black sheets
    # Check the four corners of the white sheet
    corners = [
        (x1, y1),  # bottom left
        (x1, y2),  # top left
        (x2, y1),  # bottom right
        (x2, y2)   # top right
    ]
    
    for cx, cy in corners:
        # Check if the corner is outside the white sheet and outside both black sheets
        if (cx < x1 or cx > x2 or cy < y1 or cy > y2) and not (x3 < cx < x4 and y3 < cy < y4) and not (x5 < cx < x6 and y5 < cy < y6):
            return "YES"
    
    # Check the edges of the white sheet
    edges = [
        (x1, y1 - 1),  # below bottom edge
        (x1, y2 + 1),  # above top edge
        (x1 - 1, y1),  # left of left edge
        (x2 + 1, y1)   # right of right edge
    ]
    
    for ex, ey in edges:
        if not (x3 < ex < x4 and y3 < ey < y4) and not (x5 < ex < x6 and y5 < ey < y6):
            return "YES"
    
    return "NO"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output result
print(can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))