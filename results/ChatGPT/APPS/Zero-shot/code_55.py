# Read the coordinates of the white sheet
x1, y1, x2, y2 = map(int, input().split())
# Read the coordinates of the first black sheet
x3, y3, x4, y4 = map(int, input().split())
# Read the coordinates of the second black sheet
x5, y5, x6, y6 = map(int, input().split())

# Check if the white sheet is completely covered by the black sheets
covered_x_min = max(x3, x5)
covered_x_max = min(x4, x6)
covered_y_min = max(y3, y5)
covered_y_max = min(y4, y6)

# Check if the black sheets together cover the white sheet completely
if (covered_x_min < covered_x_max) and (covered_y_min < covered_y_max):
    # Check if the area of the white sheet is inside the area covered by black sheets
    if (x1 >= covered_x_min and x2 <= covered_x_max and y1 >= covered_y_min and y2 <= covered_y_max):
        print("NO")
    else:
        print("YES")
else:
    print("YES")