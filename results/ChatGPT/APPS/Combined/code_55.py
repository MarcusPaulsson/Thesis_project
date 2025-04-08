def is_visible(white, black1, black2):
    # Check if the white sheet is completely covered by either black sheet
    def is_completely_covered(white, black):
        wx1, wy1, wx2, wy2 = white
        bx1, by1, bx2, by2 = black
        return bx1 <= wx1 and bx2 >= wx2 and by1 <= wy1 and by2 >= wy2

    # Check visibility
    if is_completely_covered(white, black1) or is_completely_covered(white, black2):
        return "NO"

    wx1, wy1, wx2, wy2 = white
    b1 = black1
    b2 = black2
    
    # Check if any part of the white sheet is visible
    if (wx2 <= b1[0] or b1[2] <= wx1 or wy2 <= b1[1] or b1[3] <= wy1) or \
       (wx2 <= b2[0] or b2[2] <= wx1 or wy2 <= b2[1] or b2[3] <= wy1):
        return "YES"

    return "NO"


# Input reading
white_sheet = tuple(map(int, input().split()))
black_sheet1 = tuple(map(int, input().split()))
black_sheet2 = tuple(map(int, input().split()))

# Output the result
print(is_visible(white_sheet, black_sheet1, black_sheet2))