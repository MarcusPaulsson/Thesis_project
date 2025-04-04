def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the white sheet is fully covered by the first black sheet
    if x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2:
        return "NO"
    # Check if the white sheet is fully covered by the second black sheet
    if x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2:
        return "NO"
    # Check if the white sheet is fully covered by both black sheets
    if (x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2) or (x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2):
        return "NO"
    # Check if the white sheet is fully covered by the intersection of both black sheets
    if (max(x3, x5) <= x1 and max(y3, y5) <= y1 and min(x4, x6) >= x2 and min(y4, y6) >= y2):
        return "NO"
    return "YES"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Print output
print(is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))