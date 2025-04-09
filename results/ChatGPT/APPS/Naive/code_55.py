def is_white_sheet_visible(white_sheet, black_sheets):
    x1, y1, x2, y2 = white_sheet
    x3, y3, x4, y4 = black_sheets[0]
    x5, y5, x6, y6 = black_sheets[1]

    # Check for any visible point not strictly inside the white sheet
    # and strictly outside both black sheets.
    
    # Conditions for visibility:
    visible_area = (
        (x2 < x3) or  # Right of first black sheet
        (x1 > x4) or  # Left of first black sheet
        (y2 < y3) or  # Above first black sheet
        (y1 > y4) or  # Below first black sheet
        (x2 < x5) or  # Right of second black sheet
        (x1 > x6) or  # Left of second black sheet
        (y2 < y5) or  # Above second black sheet
        (y1 > y6)     # Below second black sheet
    )
    
    return "YES" if visible_area else "NO"

# Read input
white_sheet = list(map(int, input().split()))
black_sheets = [list(map(int, input().split())), list(map(int, input().split()))]

# Output result
print(is_white_sheet_visible(white_sheet, black_sheets))