def can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any visible part of the white sheet
    # Check left side
    if x1 > x4 and x1 > x6:
        return "YES"
    # Check right side
    if x2 < x3 and x2 < x5:
        return "YES"
    # Check bottom side
    if y1 > y4 and y1 > y6:
        return "YES"
    # Check top side
    if y2 < y3 and y2 < y5:
        return "YES"
    
    # Check if the white sheet is completely covered by the black sheets
    covered_left = (x3 <= x1 < x4) or (x5 <= x1 < x6)
    covered_right = (x3 < x2 <= x4) or (x5 < x2 <= x6)
    covered_bottom = (y3 <= y1 < y4) or (y5 <= y1 < y6)
    covered_top = (y3 < y2 <= y4) or (y5 < y2 <= y6)
    
    if covered_left and covered_right and covered_bottom and covered_top:
        return "NO"
    
    return "YES"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Get the result and print it
result = can_see_white_sheet(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)
print(result)