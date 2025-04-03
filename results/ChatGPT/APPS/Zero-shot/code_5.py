def is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    # Check if the white sheet is completely covered by the two black sheets
    is_covered_by_first = (x3 <= x1 and y3 <= y1 and x4 >= x2 and y4 >= y2)
    is_covered_by_second = (x5 <= x1 and y5 <= y1 and x6 >= x2 and y6 >= y2)
    
    # Check if there is any overlap between the white sheet and black sheets
    overlap_first = not (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1)
    overlap_second = not (x2 <= x5 or x6 <= x1 or y2 <= y5 or y6 <= y1)

    # If the white sheet is fully covered by both black sheets, return "NO"
    if is_covered_by_first or is_covered_by_second:
        return "NO"
    
    # Check if the white sheet has visible area
    if (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4) or \
       (x2 < x5 or x1 > x6 or y2 < y5 or y1 > y6):
        return "YES"
    
    # If both black sheets overlap with the white sheet, we need to check if they cover the entire area
    left_bound = min(x3, x5)
    right_bound = max(x4, x6)
    bottom_bound = min(y3, y5)
    top_bound = max(y4, y6)

    if left_bound <= x1 and right_bound >= x2 and bottom_bound <= y1 and top_bound >= y2:
        return "NO"

    return "YES"

# Input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Output
print(is_visible(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))