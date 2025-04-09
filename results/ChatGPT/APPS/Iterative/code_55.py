def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if any part of the white sheet is visible by checking the four edges and corners
    # A point is visible if it's not inside the white sheet and not inside both black sheets

    # Check edges and corners of the white sheet
    visible = (
        (x1 - 1 < x3 or x1 - 1 < x5 or x2 + 1 > x4 or x2 + 1 > x6 or 
         y1 - 1 < y3 or y1 - 1 < y5 or y2 + 1 > y4 or y2 + 1 > y6)
    )

    # Check if any part of the white sheet is not covered by black sheets
    def is_inside_black(wx, wy):
        return (x3 < wx < x4 and y3 < wy < y4) or (x5 < wx < x6 and y5 < wy < y6)

    # Check corners of the white sheet
    white_corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    
    for wx, wy in white_corners:
        if not is_inside_black(wx, wy):
            return "YES"

    # Check edges of the white sheet
    white_edges_x = [x1 - 1, x2, x1, x2 + 1]
    white_edges_y = [y1 - 1, y2, y1, y2 + 1]

    for wx in white_edges_x:
        for wy in [y1, y2]:
            if not is_inside_black(wx, wy):
                return "YES"

    for wy in white_edges_y:
        for wx in [x1, x2]:
            if not is_inside_black(wx, wy):
                return "YES"

    return "NO"


# Input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output
print(is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))