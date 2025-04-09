x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Check if any part of the white sheet is visible
def is_visible():
    # Check the four corners of the white sheet against the black sheets
    corners = [
        (x1, y1), (x1, y2), (x2, y1), (x2, y2)
    ]
    
    for x, y in corners:
        if not (x3 < x < x4 and y3 < y < y4) and not (x5 < x < x6 and y5 < y < y6):
            return True
    return False

if is_visible():
    print("YES")
else:
    print("NO")