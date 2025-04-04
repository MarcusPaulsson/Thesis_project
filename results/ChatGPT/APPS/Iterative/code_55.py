def is_visible(white_sheet, black_sheets):
    # Unpack the coordinates for better readability
    x1, y1, x2, y2 = white_sheet
    (x3, y3, x4, y4), (x5, y5, x6, y6) = black_sheets
    
    # Check if the white sheet is completely covered by any of the black sheets
    covered_by_first = (x3 <= x1 <= x2 <= x4 and y3 <= y1 <= y2 <= y4)
    covered_by_second = (x5 <= x1 <= x2 <= x6 and y5 <= y1 <= y2 <= y6)
    
    if covered_by_first and covered_by_second:
        print("NO")
        return

    # Check if there is any visible part
    visible = (
        (x1 < x3 or x2 > x4 or y1 < y3 or y2 > y4) or
        (x1 < x5 or x2 > x6 or y1 < y5 or y2 > y6)
    )
    
    print("YES" if visible else "NO")

# Read input
white_sheet = list(map(int, input().split()))
black_sheets = [tuple(map(int, input().split())) for _ in range(2)]

# Call the function
is_visible(white_sheet, black_sheets)