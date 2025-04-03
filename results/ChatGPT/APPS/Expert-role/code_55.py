def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if there is any part of the white sheet that is not covered by both black sheets
    # The white sheet is visible if it has any area that is outside both black sheets
    
    # Check if the entire white sheet is covered by the first black sheet
    covered_by_first = (x3 < x1 < x4 and y3 < y1 < y4) and (x3 < x2 < x4 and y3 < y2 < y4)
    # Check if the entire white sheet is covered by the second black sheet
    covered_by_second = (x5 < x1 < x6 and y5 < y1 < y6) and (x5 < x2 < x6 and y5 < y2 < y6)
    
    # If both black sheets cover the white sheet completely, it's not visible
    if covered_by_first and covered_by_second:
        return "NO"
    
    # Check for visibility on the left side of the white sheet
    if (x3 >= x2 or x5 >= x2) or (y3 >= y2 or y5 >= y2) or (x3 <= x1 and x5 <= x1):
        return "YES"
    
    # Check for visibility on the right side of the white sheet
    if (x4 <= x1 or x6 <= x1) or (y4 <= y1 or y6 <= y1) or (x4 >= x2 and x6 >= x2):
        return "YES"
    
    # Check for visibility on the top side of the white sheet
    if (y3 <= y1 or y4 <= y1 or y5 <= y1 or y6 <= y1) or (y3 >= y2 and y4 >= y2 and y5 >= y2 and y6 >= y2):
        return "YES"
    
    # Check for visibility on the bottom side of the white sheet
    if (y3 >= y2 or y5 >= y2) or (x3 >= x2 and x5 >= x2):
        return "YES"

    return "NO"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))