# Read input coordinates for the white sheet and the two black sheets
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Determine the coverage of the black sheets
covered_left = min(x3, x5)
covered_right = max(x4, x6)
covered_bottom = min(y3, y5)
covered_top = max(y4, y6)

# Check if the white sheet is fully covered by the black sheets
if (x2 <= covered_left or x1 >= covered_right or
    y2 <= covered_bottom or y1 >= covered_top):
    print("YES")
else:
    print("NO")