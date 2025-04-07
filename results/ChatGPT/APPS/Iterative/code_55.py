def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the black sheets completely cover the white sheet
    is_covered = (x3 >= x2 or x4 <= x1 or y3 >= y2 or y4 <= y1) and (x5 >= x2 or x6 <= x1 or y5 >= y2 or y6 <= y1)
    
    if is_covered:
        return "NO"
    
    # Check if there is any part of the white sheet visible
    visible = (x3 < x1 and x4 > x1) or (x5 < x1 and x6 > x1) or (x3 < x2 and x4 > x2) or (x5 < x2 and x6 > x2) or \
              (y3 < y1 and y4 > y1) or (y5 < y1 and y6 > y1) or (y3 < y2 and y4 > y2) or (y5 < y2 and y6 > y2)
    
    return "YES" if visible else "NO"

# Read input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output the result
print(is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))