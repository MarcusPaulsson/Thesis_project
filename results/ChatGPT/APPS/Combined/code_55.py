def is_white_sheet_visible(white_sheet, black_sheets):
    x1, y1, x2, y2 = white_sheet

    # Check if the white sheet is completely covered by either black sheet
    covered_by_first_black = (black_sheets[0][0] <= x1 < black_sheets[0][2] and 
                               black_sheets[0][1] <= y1 < black_sheets[0][3] and 
                               black_sheets[0][0] <= x2 < black_sheets[0][2] and 
                               black_sheets[0][1] <= y2 < black_sheets[0][3])
    
    covered_by_second_black = (black_sheets[1][0] <= x1 < black_sheets[1][2] and 
                                black_sheets[1][1] <= y1 < black_sheets[1][3] and 
                                black_sheets[1][0] <= x2 < black_sheets[1][2] and 
                                black_sheets[1][1] <= y2 < black_sheets[1][3])

    # Check if the white sheet is completely covered by both black sheets
    if (black_sheets[0][0] <= x1 and black_sheets[0][2] >= x2 and 
        black_sheets[0][1] <= y1 and black_sheets[0][3] >= y2) or \
       (black_sheets[1][0] <= x1 and black_sheets[1][2] >= x2 and 
        black_sheets[1][1] <= y1 and black_sheets[1][3] >= y2):
        return "NO"

    # Check if there is any part of the white sheet that is visible
    visible = (
        (x1 > black_sheets[0][2] or x2 < black_sheets[0][0] or y1 > black_sheets[0][3] or y2 < black_sheets[0][1]) or
        (x1 > black_sheets[1][2] or x2 < black_sheets[1][0] or y1 > black_sheets[1][3] or y2 < black_sheets[1][1])
    )

    return "YES" if visible else "NO"

# Input reading
white_sheet = list(map(int, input().split()))
black_sheets = [list(map(int, input().split())) for _ in range(2)]

# Output the result
print(is_white_sheet_visible(white_sheet, black_sheets))