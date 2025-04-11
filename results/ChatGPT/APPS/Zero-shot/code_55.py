x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Check if there is any point outside the white sheet and not covered by both black sheets
def is_visible():
    # Check the four corners of the white sheet
    corners = [
        (x1, y1),  # bottom left
        (x1, y2),  # top left
        (x2, y1),  # bottom right
        (x2, y2)   # top right
    ]
    
    for (x, y) in corners:
        # Check if the point (x, y) is outside the white sheet
        if (x < x1 or x > x2 or y < y1 or y > y2):
            # Check if the point is strictly outside both black sheets
            if not (x3 < x < x4 and y3 < y < y4) and not (x5 < x < x6 and y5 < y < y6):
                return True
    return False

if is_visible():
    print("YES")
else:
    print("NO")