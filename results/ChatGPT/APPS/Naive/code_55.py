def can_see_white_sheet(white, black1, black2):
    x1, y1, x2, y2 = white
    x3, y3, x4, y4 = black1
    x5, y5, x6, y6 = black2

    # Check if any part of the white sheet is visible
    visible = (
        (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1) or  # White is completely to the left, right, above or below black1
        (x2 <= x5 or x6 <= x1 or y2 <= y5 or y6 <= y1)    # White is completely to the left, right, above or below black2
    )
    
    return "YES" if visible else "NO"

# Read input
white_sheet = list(map(int, input().split()))
black_sheet1 = list(map(int, input().split()))
black_sheet2 = list(map(int, input().split()))

# Output result
print(can_see_white_sheet(white_sheet, black_sheet1, black_sheet2))